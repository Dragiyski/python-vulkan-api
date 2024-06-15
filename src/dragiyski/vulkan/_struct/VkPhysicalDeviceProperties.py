import ctypes, sys

class VkPhysicalDeviceProperties(ctypes.Structure):
    pass

sys.modules[__name__] = VkPhysicalDeviceProperties

from . import VkPhysicalDeviceLimits
from . import VkPhysicalDeviceSparseProperties

VkPhysicalDeviceProperties._fields_ = [
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
