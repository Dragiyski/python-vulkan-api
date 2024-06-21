import ctypes

class CType(ctypes.Structure):
    pass

from .VkDeviceOrHostAddressConstKHR import CType as VkDeviceOrHostAddressConstKHR
from .VkDeviceOrHostAddressKHR import CType as VkDeviceOrHostAddressKHR
from .VkMicromapUsageEXT import CType as VkMicromapUsageEXT

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('type', ctypes.c_int),
    ('flags', ctypes.c_uint32),
    ('mode', ctypes.c_int),
    ('dstMicromap', ctypes.c_void_p),
    ('usageCountsCount', ctypes.c_uint32),
    ('pUsageCounts', ctypes.POINTER(VkMicromapUsageEXT)),
    ('ppUsageCounts', ctypes.POINTER(ctypes.POINTER(VkMicromapUsageEXT))),
    ('data', VkDeviceOrHostAddressConstKHR),
    ('scratchData', VkDeviceOrHostAddressKHR),
    ('triangleArray', VkDeviceOrHostAddressConstKHR),
    ('triangleArrayStride', ctypes.c_uint64),
]
