import ctypes

class VkClearValue(ctypes.Union):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'color': VkClearColorValue,
            'depthStencil': VkClearDepthStencilValue,
        }


from .VkClearColorValue import VkClearColorValue
from .VkClearDepthStencilValue import VkClearDepthStencilValue

VkClearValue._fields_ = [
    ('color', VkClearColorValue),
    ('depthStencil', VkClearDepthStencilValue),
]
