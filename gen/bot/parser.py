import operator
import re
import urllib.request
from bs4 import BeautifulSoup
from .models import Api, Tag, Group, Object, Parameter, ApiType
from ..const import BOT_API_HTML

EMPTY_OBJECT = Object()
ETURN = "eturn"
HREF = "href"
ARRAY_OF = "Array of "
OR = " or "
TAG_PATTERN = re.compile(r"always “([\w/]+)”|must be <em>([\w]+)</em>")
PY_TYPES = {
    "Integer": "int",
    "Int": "int",
    "String": "str",
    "Boolean": "bool",
    "True": "bool",
    "Float": "float",
    "Float number": "float",
}


def pythonize(tp: str) -> str:
    if tp.startswith("#"):
        return tp
    if tp not in PY_TYPES.keys():
        raise TypeError(f"Type: {tp!r} is not valid")
    return PY_TYPES.get(tp, tp)


def cache_html():
    urllib.request.urlretrieve("https://core.telegram.org/bots/api", BOT_API_HTML)


def parse_version(soup):
    pattern = re.compile("Bot API (.*)")
    bot_api = soup.find("strong", text=pattern).text
    return pattern.search(bot_api).group(1)


def get_soup():
    with open(BOT_API_HTML, encoding="UTF-8") as f:
        data = f.read()
    return BeautifulSoup(data, "lxml").find("div", id="dev_page_content")


def parse_tag(name, desc):
    if found := re.search(TAG_PATTERN, str(desc)):
        return Tag(name, found.group(1) or found.group(2))
    return None


def parse_params(child):
    params = []
    is_path = len(child.thead.tr.findAll("th")) == 4
    for tr in child.tbody.findAll("tr"):
        td = tr.findAll("td")
        desc = td[3] if is_path else td[2]
        params.append(Parameter(
            name=td[0].text,
            tag=parse_tag(td[0].text, desc),
            description=desc,
            type=ApiType(
                array=td[1].text.count(ARRAY_OF),
                required="Optional" not in td[2].text,
                types=[pythonize(t.replace(ARRAY_OF, ""))
                       for t in re.split(r", | or | and ", "".join([
                            (c if isinstance(c, str) else c["href"]) 
                            for c in td[1].contents]))]
            )
        ))
    params.sort(key=operator.attrgetter("type.required"), reverse=True)
    return params


def parse_response(child):
    replaced = "".join([c[HREF] if c.name == "a" else c.text for c in child.contents])
    returned = [p.strip() for p in re.split("\.|,", replaced) if ETURN in p]
    pattern = re.compile('(?:True|Int|String|#\w+)')
    response = ApiType(array=int("rray" in replaced))
    for phrase in returned:
        if (found := re.search(pattern, phrase)) and found.group() != "#getchat":
            if (tp := found.group()) not in response.types:
                response.types.append(pythonize(tp))
    return response


def main_parse():
    soup = get_soup()
    version = parse_version(soup)
    api = Api(version=version)
    found_target = False
    group = Group()
    object_ = EMPTY_OBJECT
    for child in soup.childGenerator():
        if child.name == "h3" and child.text == "Getting updates":
            found_target = True
        if found_target:
            if child.name == "h3":
                group = Group(name=child.text)
                api.groups.append(group)
                object_ = EMPTY_OBJECT
            if child.name == "h4":
                if " " in child.text:
                    object_ = EMPTY_OBJECT
                else:
                    object_ = Object(child.text, child.a["name"])
                    group.objects.append(object_)
            if object_:
                if child.name == "p":
                    object_.descriptions.append(child)
                    if len(object_.descriptions) == 1 and object_.is_path:
                        object_.response = parse_response(child)
                if child.name == "blockquote":
                    object_.blockquote = child.text
                if child.name == "table":
                    object_.params = parse_params(child)
                if child.name == "ul":
                    object_.sub_objects = [li.a[HREF] for li in child.findAll("li")]
            else:
                group.descriptions.append(child.text)
    return api


def post_parsing(api: Api):
    for g in api.groups:
        for o in g.objects:
            for p in o.params:
                p.type.types = [
                    api.get(t)
                    if isinstance(t, str) and t.startswith("#")
                    else t
                    for t in p.type.types
                ]
            if o.childs:
                childs = []
                for s in o.childs:
                    if isinstance(s, str):
                        child = api.get(s)
                        child.parrent = o
                        childs.append(child)
                o.childs = childs
            if o.response:
                for i, rt in enumerate(o.response.types):
                    if isinstance(rt, str) and rt.startswith("#"):
                        o.response.types[i] = api.get(rt)


def parse_api():
    api = main_parse()
    api.indexing()
    post_parsing(api)
    return api
