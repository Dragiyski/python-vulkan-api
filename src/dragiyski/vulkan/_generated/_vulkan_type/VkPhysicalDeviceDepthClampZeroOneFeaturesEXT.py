import ctypes, sys

class VkPhysicalDeviceDepthClampZeroOneFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('depthClampZeroOne', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceDepthClampZeroOneFeaturesEXT
