from abc import ABC, abstractmethod

from proxy_canvas import ProxyCanvas


class Plugin(ABC):

    @abstractmethod
    def key_pressed(self, key_code: str, canvas: ProxyCanvas, cursor_x: int, cursor: y):
        pass

    @abstractmethod
    def key_released(self, key_code: str, canvas: ProxyCanvas, cursor_x: int, cursor: y):
        pass

    @abstractmethod
    def mouse_moved_with_button_pressed(self, canvas: ProxyCanvas, old_x: int, old_y: int, new_x: int, new_y: int):
        pass

    @abstractmethod
    def mouse_button_pressed(self, canvas: ProxyCanvas, x: int, y: int):
        pass

    @abstractmethod
    def mouse_button_released(self, canvas: ProxyCanvas, x: int, y: int):
        pass
