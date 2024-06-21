import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent3D import CType as VkExtent3D
from .VkImageSubresource import CType as VkImageSubresource
from .VkOffset3D import CType as VkOffset3D

CType._fields_ = [
    ('subresource', VkImageSubresource),
    ('offset', VkOffset3D),
    ('extent', VkExtent3D),
    ('memory', ctypes.c_void_p),
    ('memoryOffset', ctypes.c_uint64),
    ('flags', ctypes.c_uint32),
]