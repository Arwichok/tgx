from __future__ import annotations

from dataclasses import dataclass, field
import keyword
import re
from typing import Dict, List, Optional, Union
from bs4 import PageElement
import inflection
from markdownify import markdownify as md

TYPINGS_LIST = [
    "Optional",
    "Union",
    "List"
]


@dataclass
class ApiEnum:
    name: str
    obj: Optional[str] = None
    param: Optional[str] = None
    desc: Optional[str] = None
    pattern: Optional[re.Pattern] = None
    enum: Dict[str, str] = field(default_factory=dict)


@dataclass
class Tag:
    name: str = ""
    value: str = ""


@dataclass
class ApiType:
    types: List[Union[str, Object]] = field(default_factory=list)
    array: int = 0
    required: bool = True

    @property
    def optional(self):
        return not self.required

    @property
    def union(self):
        return len(self.types) > 1

    @property
    def annotation(self):
        ano = ", ".join(map(str, self.types))
        if self.optional and self.union and not self.array:
            ano += ", None"
        if self.union:
            ano = f"Union[{ano}]"
        if self.array:
            ano = f"List[{ano}]"
        if self.optional and not self.union:
            ano = f"Optional[{ano}]"
        return ano

    def __str__(self) -> str:
        return self.annotation


@dataclass
class Parameter:
    name: str
    type: ApiType
    tag: Optional[Tag] = None
    description: str = ""

    @property
    def required(self):
        return self.type.required

    @property
    def optional(self):
        return self.type.optional
    
    @property
    def annotation(self):
        return self.type.annotation

    @property
    def types(self):
        return self.type.types

    @property
    def alias(self) -> str:
        return self.name + ("_" if keyword.iskeyword(self.name) else "")

    @property
    def value(self) -> str:
        args = []
        if self.alias != self.name:
            args.append(f"name={self.name!r}")
        if self.type.optional:
            args.append("default=None")
        tmp = ", ".join(args)
        return f" = field({tmp})"
    
    @property
    def text_desc(self):
        return self.description.text
    
    @property
    def md_desc(self):
        return md(str(self.description))
    


@dataclass
class Object:
    name: str = ""
    anchor: str = field(default="", repr=False)
    response: Optional[ApiType] = field(default_factory=ApiType, repr=False)
    blockquote: Optional[str] = None
    descriptions: List[PageElement] = field(default_factory=list)
    params: List[Parameter] = field(default_factory=list)
    childs: List[Union[str, Object]] = field(default_factory=list, repr=False)
    parrent: Optional[Object] = field(default=None, repr=False)

    def __bool__(self):
        return bool(self.name)
    
    def __str__(self) -> str:
        return self.camel
    
    def __hash__(self) -> int:
        return hash(self.name)
    
    @property
    def is_path(self):
        return self.name[0].islower()

    @property
    def is_schema(self):
        return self.name[0].istitle()

    @property
    def is_field(self):
        for p in self.params:
            if "field" in p.value:
                return True
        return False

    @property
    def camel(self) -> str:
        return inflection.camelize(self.name)

    @property
    def snake(self) -> str:
        return inflection.underscore(self.name)

    @property
    def tag(self) -> Optional[Tag]:
        for p in self.params:
            if p.tag:
                return p.tag

    @property
    def typings(self):
        tps = set()
        for p in [*self.params, self.response]:
            for t in TYPINGS_LIST:
                if t in p.annotation:
                    tps.add(t)
        return tps

    @property
    def schemas(self):
        return set([
            t
            for p in [*self.params, self.response]
            for t in [*p.types, self.parrent]
            if isinstance(t, Object)
        ])
    
    @property
    def text_desc(self):
        return [d.text for d in self.descriptions]
    
    @property
    def md_desc(self):
        return [md(str(d)) for d in self.descriptions]
    

@dataclass
class Group:
    name: str = ""
    objects: List[Object] = field(default_factory=list)
    descriptions: List[str] = field(default_factory=list)

    def __bool__(self):
        return bool(self.name)


@dataclass
class Api:
    version: str
    groups: List[Group] = field(default_factory=list)
    indexed: Dict[str, Object] = field(default_factory=dict)

    @property
    def objects(self):
        for g in self.groups:
            for o in g.objects:
                yield o

    def get(self, anchor: str):
        key = anchor[1:] if anchor.startswith("#") else anchor
        return self.indexed[key]

    def indexing(self):
        for g in self.groups:
            for o in g.objects:
                self.indexed[o.anchor] = o
