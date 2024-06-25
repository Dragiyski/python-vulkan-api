import ctypes

class VkPhysicalDeviceVideoEncodeQualityLevelInfoKHR(ctypes.Structure):
    pass

from .VkVideoProfileInfoKHR import VkVideoProfileInfoKHR

VkPhysicalDeviceVideoEncodeQualityLevelInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pVideoProfile', ctypes.POINTER(VkVideoProfileInfoKHR)),
    ('qualityLevel', ctypes.c_uint32),
]

VkPhysicalDeviceVideoEncodeQualityLevelInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pVideoProfile': ctypes.POINTER(VkVideoProfileInfoKHR),
    'qualityLevel': ctypes.c_uint32,
}
