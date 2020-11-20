from tkinter import Tk, Canvas
from typing import Optional, List

from plugin import Plugin
from proxy_canvas import ProxyCanvas
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

        self._canvas.bind("<KeyRelease>", self.key_pressed_handler)
        self._canvas.bind('<B1-Motion>', self.mouse_moved_with_pressed_button_handler)
        self._canvas.bind('<ButtonRelease-1>', self.mouse_button_released_handler)
        self._canvas.focus_set()

        self._proxy_canvas = ProxyCanvas(self._canvas)

    def mouse_moved_with_pressed_button_handler(self, event):
        plugins = self._get_plugins_to_apply()
        for plugin in plugins:
            plugin.mouse_moved_with_button_pressed(self._proxy_canvas, )
        pass

    def key_pressed_handler(self, event):
        pass

    def mouse_button_pressed_handler(self, event):
        pass

    def mouse_button_released_handler(self, event):
        pass

    def _get_plugins_to_apply(self) -> List[Plugin]:
        pass
