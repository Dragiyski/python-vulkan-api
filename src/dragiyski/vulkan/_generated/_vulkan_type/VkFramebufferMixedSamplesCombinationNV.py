import ctypes

class VkFramebufferMixedSamplesCombinationNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('coverageReductionMode', ctypes.c_int),
        ('rasterizationSamples', ctypes.c_uint32),
        ('depthStencilSamples', ctypes.c_uint32),
        ('colorSamples', ctypes.c_uint32),
    ]

VkFramebufferMixedSamplesCombinationNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'coverageReductionMode': ctypes.c_int,
    'rasterizationSamples': ctypes.c_uint32,
    'depthStencilSamples': ctypes.c_uint32,
    'colorSamples': ctypes.c_uint32,
}
