import ctypes, sys

class VkClearValue(ctypes.Union):
    pass

sys.modules[__name__] = VkClearValue

from . import VkClearColorValue
from . import VkClearDepthStencilValue

VkClearValue._fields_ = [
    ('color', VkClearColorValue),
    ('depthStencil', VkClearDepthStencilValue),
]
