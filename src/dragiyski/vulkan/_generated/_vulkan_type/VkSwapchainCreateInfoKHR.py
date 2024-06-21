import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent2D import CType as VkExtent2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('surface', ctypes.c_void_p),
    ('minImageCount', ctypes.c_uint32),
    ('imageFormat', ctypes.c_int),
    ('imageColorSpace', ctypes.c_int),
    ('imageExtent', VkExtent2D),
    ('imageArrayLayers', ctypes.c_uint32),
    ('imageUsage', ctypes.c_uint32),
    ('imageSharingMode', ctypes.c_int),
    ('queueFamilyIndexCount', ctypes.c_uint32),
    ('pQueueFamilyIndices', ctypes.POINTER(ctypes.c_uint32)),
    ('preTransform', ctypes.c_uint32),
    ('compositeAlpha', ctypes.c_uint32),
    ('presentMode', ctypes.c_int),
    ('clipped', ctypes.c_uint32),
    ('oldSwapchain', ctypes.c_void_p),
]
