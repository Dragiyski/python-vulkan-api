import ctypes, sys

class VkPhysicalDeviceImageProcessing2FeaturesQCOM(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('textureBlockMatch2', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceImageProcessing2FeaturesQCOM
