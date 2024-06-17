import ctypes, sys

class VkPhysicalDeviceMultisampledRenderToSingleSampledFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('multisampledRenderToSingleSampled', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceMultisampledRenderToSingleSampledFeaturesEXT
