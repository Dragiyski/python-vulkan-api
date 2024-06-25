import ctypes

class VkClearValue(ctypes.Union):
    pass

from .VkClearColorValue import VkClearColorValue
from .VkClearDepthStencilValue import VkClearDepthStencilValue

VkClearValue._fields_ = [
    ('color', VkClearColorValue),
    ('depthStencil', VkClearDepthStencilValue),
]

VkClearValue._type_ = {
    'color': VkClearColorValue,
    'depthStencil': VkClearDepthStencilValue,
}
