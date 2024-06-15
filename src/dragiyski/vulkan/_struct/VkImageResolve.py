import ctypes, sys

class VkImageResolve(ctypes.Structure):
    pass

sys.modules[__name__] = VkImageResolve

from . import VkImageSubresourceLayers
from . import VkOffset3D
from . import VkExtent3D

VkImageResolve._fields_ = [
    ('srcSubresource', VkImageSubresourceLayers),
    ('srcOffset', VkOffset3D),
    ('dstSubresource', VkImageSubresourceLayers),
    ('dstOffset', VkOffset3D),
    ('extent', VkExtent3D),
]
