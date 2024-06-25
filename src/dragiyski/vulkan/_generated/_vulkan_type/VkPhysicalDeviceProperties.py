import ctypes

class VkPhysicalDeviceProperties(ctypes.Structure):
    pass

from .VkPhysicalDeviceLimits import VkPhysicalDeviceLimits
from .VkPhysicalDeviceSparseProperties import VkPhysicalDeviceSparseProperties

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

VkPhysicalDeviceProperties._type_ = {
    'apiVersion': ctypes.c_uint32,
    'driverVersion': ctypes.c_uint32,
    'vendorID': ctypes.c_uint32,
    'deviceID': ctypes.c_uint32,
    'deviceType': ctypes.c_int,
    'deviceName': ctypes.ARRAY(ctypes.c_char, 256),
    'pipelineCacheUUID': ctypes.ARRAY(ctypes.c_uint8, 16),
    'limits': VkPhysicalDeviceLimits,
    'sparseProperties': VkPhysicalDeviceSparseProperties,
}
