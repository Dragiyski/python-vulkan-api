import ctypes

class VkShaderResourceUsageAMD(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'numUsedVgprs': ctypes.c_uint32,
            'numUsedSgprs': ctypes.c_uint32,
            'ldsSizePerLocalWorkGroup': ctypes.c_uint32,
            'ldsUsageSizeInBytes': ctypes.c_size_t,
            'scratchMemUsageInBytes': ctypes.c_size_t,
        }

    _fields_ = [
        ('numUsedVgprs', ctypes.c_uint32),
        ('numUsedSgprs', ctypes.c_uint32),
        ('ldsSizePerLocalWorkGroup', ctypes.c_uint32),
        ('ldsUsageSizeInBytes', ctypes.c_size_t),
        ('scratchMemUsageInBytes', ctypes.c_size_t),
    ]
