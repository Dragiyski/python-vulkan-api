import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('minSubgroupSize', ctypes.c_uint32),
        ('maxSubgroupSize', ctypes.c_uint32),
        ('maxComputeWorkgroupSubgroups', ctypes.c_uint32),
        ('requiredSubgroupSizeStages', ctypes.c_uint32),
    ]
