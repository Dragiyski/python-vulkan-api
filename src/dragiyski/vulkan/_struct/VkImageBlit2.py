import ctypes, sys

class VkImageBlit2(ctypes.Structure):
    pass

sys.modules[__name__] = VkImageBlit2

from . import VkImageSubresourceLayers
from . import VkOffset3D

VkImageBlit2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('srcSubresource', VkImageSubresourceLayers),
    ('srcOffsets', ctypes.ARRAY(VkOffset3D, 2)),
    ('dstSubresource', VkImageSubresourceLayers),
    ('dstOffsets', ctypes.ARRAY(VkOffset3D, 2)),
]
