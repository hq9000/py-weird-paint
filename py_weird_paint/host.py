from tkinter import Tk, Canvas
from typing import Optional, List

from py_weird_paint.plugin_block import PluginBlock


class Host:
    def __init__(self, background_color: str, width: int, height: int):
        self._canvas: Optional[Canvas] = None
        self._tk: Optional[Tk] = None
        self.plugin_blocks: List[PluginBlock] = []
        self.background_color: str = background_color
        self.width: int = width
        self.height: int = height

    def run(self):
        self._tk: Tk = Tk()
        self._canvas: Canvas = Canvas(self._tk, bg=self.background_color, width=self.width, height=self.height)
        self._canvas.grid()
        self._tk.mainloop()
