from __future__ import annotations

import json
import typing
from jinja2 import Environment, PackageLoader, select_autoescape

from ..const import BOT_PATHS_DIR, BOT_SCHEMAS_DIR, CACHE_DIR
from .models import Object
from .parser import parse_api
from ..util import mk

import msgspec


class Generator:
    def __init__(self):
        self.api = parse_api()
        self.env = Environment(
            loader=PackageLoader("gen.bot"),
            autoescape=select_autoescape(),
        )

    def init(self):
        mk(CACHE_DIR)
        mk(BOT_PATHS_DIR)
        mk(BOT_SCHEMAS_DIR)


    def get_tmp(self, name: str):
        return self.env.get_template(f"{name}.jinja")
    
    # def render_object(self, obj: Object):
    #     tmp = self.get_tmp("schema.py" if obj.is_schema else "path.py")
    #     return tmp.render(obj=obj, api=self.api)

    def run(self):
        schemas = [o for o in self.api.objects if o.is_schema]
        with open(str(BOT_SCHEMAS_DIR) + ".py", "w", encoding="utf8") as f:
            f.write(self.get_tmp("schemas.py").render(schemas=schemas))




from .r import A, B


def run():
    b = B("Hello", A(12))
    a = A(34, b)

    d = msgspec.json.encode(a)

    print(d)

    print(msgspec.json.decode(d, type=A))
    Generator().run()
