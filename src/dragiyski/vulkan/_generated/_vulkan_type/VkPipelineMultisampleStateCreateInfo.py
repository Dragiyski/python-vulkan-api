import ctypes

class VkPipelineMultisampleStateCreateInfo(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'flags': ctypes.c_uint32,
            'rasterizationSamples': ctypes.c_uint32,
            'sampleShadingEnable': ctypes.c_uint32,
            'minSampleShading': ctypes.c_float,
            'pSampleMask': ctypes.POINTER(ctypes.c_uint32),
            'alphaToCoverageEnable': ctypes.c_uint32,
            'alphaToOneEnable': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('rasterizationSamples', ctypes.c_uint32),
        ('sampleShadingEnable', ctypes.c_uint32),
        ('minSampleShading', ctypes.c_float),
        ('pSampleMask', ctypes.POINTER(ctypes.c_uint32)),
        ('alphaToCoverageEnable', ctypes.c_uint32),
        ('alphaToOneEnable', ctypes.c_uint32),
    ]
