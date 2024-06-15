import ctypes, sys

class VkMultisampledRenderToSingleSampledInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('multisampledRenderToSingleSampledEnable', ctypes.c_uint32),
        ('rasterizationSamples', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkMultisampledRenderToSingleSampledInfoEXT
