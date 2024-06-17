import ctypes, sys

class VkPhysicalDeviceYcbcrImageArraysFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('ycbcrImageArrays', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceYcbcrImageArraysFeaturesEXT
