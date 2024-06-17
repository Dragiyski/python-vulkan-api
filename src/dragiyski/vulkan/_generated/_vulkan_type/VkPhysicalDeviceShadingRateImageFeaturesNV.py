import ctypes, sys

class VkPhysicalDeviceShadingRateImageFeaturesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shadingRateImage', ctypes.c_uint32),
        ('shadingRateCoarseSampleOrder', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceShadingRateImageFeaturesNV
