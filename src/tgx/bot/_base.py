import msgspec
import typing


field = msgspec.field
T = typing.TypeVar("T")

class Schema(msgspec.Struct): ...
class Path(msgspec.Struct, typing.Generic[T]): ...
