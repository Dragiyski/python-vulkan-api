import ctypes

class CType(ctypes.Structure):
    pass

from .VkDeviceOrHostAddressConstKHR import CType as VkDeviceOrHostAddressConstKHR
from .VkMicromapUsageEXT import CType as VkMicromapUsageEXT

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('indexType', ctypes.c_int),
    ('indexBuffer', VkDeviceOrHostAddressConstKHR),
    ('indexStride', ctypes.c_uint64),
    ('baseTriangle', ctypes.c_uint32),
    ('usageCountsCount', ctypes.c_uint32),
    ('pUsageCounts', ctypes.POINTER(VkMicromapUsageEXT)),
    ('ppUsageCounts', ctypes.POINTER(ctypes.POINTER(VkMicromapUsageEXT))),
    ('micromap', ctypes.c_void_p),
]
