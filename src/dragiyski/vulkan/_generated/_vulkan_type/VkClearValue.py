import ctypes

class CType(ctypes.Union):
    pass

from .VkClearColorValue import CType as VkClearColorValue
from .VkClearDepthStencilValue import CType as VkClearDepthStencilValue

CType._fields_ = [
    ('color', VkClearColorValue),
    ('depthStencil', VkClearDepthStencilValue),
]
