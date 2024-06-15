import ctypes, sys

class VkPhysicalDeviceMultiDrawFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('multiDraw', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceMultiDrawFeaturesEXT
