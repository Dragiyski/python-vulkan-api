import ctypes

class VkPipelineColorBlendAttachmentState(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'blendEnable': ctypes.c_uint32,
            'srcColorBlendFactor': ctypes.c_int,
            'dstColorBlendFactor': ctypes.c_int,
            'colorBlendOp': ctypes.c_int,
            'srcAlphaBlendFactor': ctypes.c_int,
            'dstAlphaBlendFactor': ctypes.c_int,
            'alphaBlendOp': ctypes.c_int,
            'colorWriteMask': ctypes.c_uint32,
        }

    _fields_ = [
        ('blendEnable', ctypes.c_uint32),
        ('srcColorBlendFactor', ctypes.c_int),
        ('dstColorBlendFactor', ctypes.c_int),
        ('colorBlendOp', ctypes.c_int),
        ('srcAlphaBlendFactor', ctypes.c_int),
        ('dstAlphaBlendFactor', ctypes.c_int),
        ('alphaBlendOp', ctypes.c_int),
        ('colorWriteMask', ctypes.c_uint32),
    ]
