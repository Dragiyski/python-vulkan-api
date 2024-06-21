import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent3D import CType as VkExtent3D

CType._fields_ = [
    ('queueFlags', ctypes.c_uint32),
    ('queueCount', ctypes.c_uint32),
    ('timestampValidBits', ctypes.c_uint32),
    ('minImageTransferGranularity', VkExtent3D),
]
