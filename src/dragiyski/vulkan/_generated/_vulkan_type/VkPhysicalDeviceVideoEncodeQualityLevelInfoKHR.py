import ctypes, sys

class VkPhysicalDeviceVideoEncodeQualityLevelInfoKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkPhysicalDeviceVideoEncodeQualityLevelInfoKHR

from . import VkVideoProfileInfoKHR

VkPhysicalDeviceVideoEncodeQualityLevelInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pVideoProfile', ctypes.POINTER(VkVideoProfileInfoKHR)),
    ('qualityLevel', ctypes.c_uint32),
]
