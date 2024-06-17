import ctypes, sys

class VkPhysicalDeviceOpticalFlowFeaturesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('opticalFlow', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceOpticalFlowFeaturesNV
