import ctypes, sys

class VkPhysicalDeviceImageProcessingFeaturesQCOM(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('textureSampleWeighted', ctypes.c_uint32),
        ('textureBoxFilter', ctypes.c_uint32),
        ('textureBlockMatch', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceImageProcessingFeaturesQCOM
