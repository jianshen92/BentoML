"""
This type stub file was generated by pyright.
"""

from typing import Any

class PhotoImage:
    tk: Any
    def __init__(
        self, image: Any | None = ..., size: Any | None = ..., **kw
    ) -> None: ...
    def __del__(self) -> None: ...
    def width(self): ...
    def height(self): ...
    def paste(self, im, box: Any | None = ...) -> None: ...

class BitmapImage:
    def __init__(self, image: Any | None = ..., **kw) -> None: ...
    def __del__(self) -> None: ...
    def width(self): ...
    def height(self): ...

def getimage(photo): ...
