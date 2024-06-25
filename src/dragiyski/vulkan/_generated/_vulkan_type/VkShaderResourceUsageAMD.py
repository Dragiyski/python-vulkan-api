import ctypes

class VkShaderResourceUsageAMD(ctypes.Structure):
    _fields_ = [
        ('numUsedVgprs', ctypes.c_uint32),
        ('numUsedSgprs', ctypes.c_uint32),
        ('ldsSizePerLocalWorkGroup', ctypes.c_uint32),
        ('ldsUsageSizeInBytes', ctypes.c_size_t),
        ('scratchMemUsageInBytes', ctypes.c_size_t),
    ]

VkShaderResourceUsageAMD._type_ = {
    'numUsedVgprs': ctypes.c_uint32,
    'numUsedSgprs': ctypes.c_uint32,
    'ldsSizePerLocalWorkGroup': ctypes.c_uint32,
    'ldsUsageSizeInBytes': ctypes.c_size_t,
    'scratchMemUsageInBytes': ctypes.c_size_t,
}
