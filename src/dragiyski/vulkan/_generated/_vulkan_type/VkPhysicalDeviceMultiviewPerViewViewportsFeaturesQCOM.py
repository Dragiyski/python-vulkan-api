import ctypes, sys

class VkPhysicalDeviceMultiviewPerViewViewportsFeaturesQCOM(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('multiviewPerViewViewports', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceMultiviewPerViewViewportsFeaturesQCOM
