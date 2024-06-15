import ctypes, sys

class VkImageCopy(ctypes.Structure):
    pass

sys.modules[__name__] = VkImageCopy

from . import VkImageSubresourceLayers
from . import VkOffset3D
from . import VkExtent3D

VkImageCopy._fields_ = [
    ('srcSubresource', VkImageSubresourceLayers),
    ('srcOffset', VkOffset3D),
    ('dstSubresource', VkImageSubresourceLayers),
    ('dstOffset', VkOffset3D),
    ('extent', VkExtent3D),
]
