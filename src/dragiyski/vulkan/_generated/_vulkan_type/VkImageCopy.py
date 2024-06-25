import ctypes

class VkImageCopy(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'srcSubresource': VkImageSubresourceLayers,
            'srcOffset': VkOffset3D,
            'dstSubresource': VkImageSubresourceLayers,
            'dstOffset': VkOffset3D,
            'extent': VkExtent3D,
        }


from .VkExtent3D import VkExtent3D
from .VkImageSubresourceLayers import VkImageSubresourceLayers
from .VkOffset3D import VkOffset3D

VkImageCopy._fields_ = [
    ('srcSubresource', VkImageSubresourceLayers),
    ('srcOffset', VkOffset3D),
    ('dstSubresource', VkImageSubresourceLayers),
    ('dstOffset', VkOffset3D),
    ('extent', VkExtent3D),
]
