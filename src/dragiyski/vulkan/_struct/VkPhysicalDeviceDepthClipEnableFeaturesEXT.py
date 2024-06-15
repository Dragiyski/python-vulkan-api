import ctypes, sys

class VkPhysicalDeviceDepthClipEnableFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('depthClipEnable', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceDepthClipEnableFeaturesEXT
