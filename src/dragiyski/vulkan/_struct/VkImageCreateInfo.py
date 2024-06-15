import ctypes, sys

class VkImageCreateInfo(ctypes.Structure):
    pass

sys.modules[__name__] = VkImageCreateInfo

from . import VkExtent3D

VkImageCreateInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('imageType', ctypes.c_int),
    ('format', ctypes.c_int),
    ('extent', VkExtent3D),
    ('mipLevels', ctypes.c_uint32),
    ('arrayLayers', ctypes.c_uint32),
    ('samples', ctypes.c_uint32),
    ('tiling', ctypes.c_int),
    ('usage', ctypes.c_uint32),
    ('sharingMode', ctypes.c_int),
    ('queueFamilyIndexCount', ctypes.c_uint32),
    ('pQueueFamilyIndices', ctypes.POINTER(ctypes.c_uint32)),
    ('initialLayout', ctypes.c_int),
]
