import ctypes, sys

class VkCopyMemoryToImageIndirectCommandNV(ctypes.Structure):
    pass

sys.modules[__name__] = VkCopyMemoryToImageIndirectCommandNV

from . import VkImageSubresourceLayers
from . import VkOffset3D
from . import VkExtent3D

VkCopyMemoryToImageIndirectCommandNV._fields_ = [
    ('srcAddress', ctypes.c_uint64),
    ('bufferRowLength', ctypes.c_uint32),
    ('bufferImageHeight', ctypes.c_uint32),
    ('imageSubresource', VkImageSubresourceLayers),
    ('imageOffset', VkOffset3D),
    ('imageExtent', VkExtent3D),
]
