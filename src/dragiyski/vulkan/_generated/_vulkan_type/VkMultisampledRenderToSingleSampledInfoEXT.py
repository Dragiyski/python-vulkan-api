import ctypes

class VkMultisampledRenderToSingleSampledInfoEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'multisampledRenderToSingleSampledEnable': ctypes.c_uint32,
            'rasterizationSamples': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('multisampledRenderToSingleSampledEnable', ctypes.c_uint32),
        ('rasterizationSamples', ctypes.c_uint32),
    ]
