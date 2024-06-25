import ctypes

class VkMultisampledRenderToSingleSampledInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('multisampledRenderToSingleSampledEnable', ctypes.c_uint32),
        ('rasterizationSamples', ctypes.c_uint32),
    ]

VkMultisampledRenderToSingleSampledInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'multisampledRenderToSingleSampledEnable': ctypes.c_uint32,
    'rasterizationSamples': ctypes.c_uint32,
}
