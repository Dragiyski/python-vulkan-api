import ctypes, sys

class VkImageBlit(ctypes.Structure):
    pass

sys.modules[__name__] = VkImageBlit

from . import VkImageSubresourceLayers
from . import VkOffset3D

VkImageBlit._fields_ = [
    ('srcSubresource', VkImageSubresourceLayers),
    ('srcOffsets', ctypes.ARRAY(VkOffset3D, 2)),
    ('dstSubresource', VkImageSubresourceLayers),
    ('dstOffsets', ctypes.ARRAY(VkOffset3D, 2)),
]
