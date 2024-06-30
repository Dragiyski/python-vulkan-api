from collections.abc import Callable

class DriverLoader:
    def __init__(self, vkGetInstanceProcAddr: Callable): ...
    