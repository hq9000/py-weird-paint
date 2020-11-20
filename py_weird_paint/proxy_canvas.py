from tkinter import Canvas
from typing import Optional

from line_style import LineStyle


class ProxyCanvas:
    def __init__(self, canvas: Canvas):
        self._canvas = canvas
        self._last_x: Optional[int] = None
        self._last_y: Optional[int] = None

    def draw_line(self, x1: int, y1: int, x2: int, y2: int, style: LineStyle, delay: int = 0):
        pass
