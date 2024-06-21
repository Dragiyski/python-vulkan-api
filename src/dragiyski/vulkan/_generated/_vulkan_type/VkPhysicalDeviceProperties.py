import ctypes

class CType(ctypes.Structure):
    pass

from .VkPhysicalDeviceLimits import CType as VkPhysicalDeviceLimits
from .VkPhysicalDeviceSparseProperties import CType as VkPhysicalDeviceSparseProperties

CType._fields_ = [
    ('apiVersion', ctypes.c_uint32),
    ('driverVersion', ctypes.c_uint32),
    ('vendorID', ctypes.c_uint32),
    ('deviceID', ctypes.c_uint32),
    ('deviceType', ctypes.c_int),
    ('deviceName', ctypes.ARRAY(ctypes.c_char, 256)),
    ('pipelineCacheUUID', ctypes.ARRAY(ctypes.c_uint8, 16)),
    ('limits', VkPhysicalDeviceLimits),
    ('sparseProperties', VkPhysicalDeviceSparseProperties),
]
