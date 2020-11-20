from typing import List

from py_weird_paint.plugin import Plugin


class PluginBlock:
    def __init__(self, activator_key: str, enabled: bool = False):
        self.activator_key: str = activator_key
        self.plugins: List[Plugin] = []
        self.enabled = enabled
        pass
