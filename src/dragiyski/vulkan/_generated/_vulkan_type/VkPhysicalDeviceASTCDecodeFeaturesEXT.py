import ctypes, sys

class VkPhysicalDeviceASTCDecodeFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('decodeModeSharedExponent', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceASTCDecodeFeaturesEXT
