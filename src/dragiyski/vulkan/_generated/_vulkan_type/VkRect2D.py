import ctypes

class VkRect2D(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'offset': VkOffset2D,
            'extent': VkExtent2D,
        }


from .VkExtent2D import VkExtent2D
from .VkOffset2D import VkOffset2D

VkRect2D._fields_ = [
    ('offset', VkOffset2D),
    ('extent', VkExtent2D),
]
