import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderEngineCount', ctypes.c_uint32),
        ('shaderArraysPerEngineCount', ctypes.c_uint32),
        ('computeUnitsPerShaderArray', ctypes.c_uint32),
        ('simdPerComputeUnit', ctypes.c_uint32),
        ('wavefrontsPerSimd', ctypes.c_uint32),
        ('wavefrontSize', ctypes.c_uint32),
        ('sgprsPerSimd', ctypes.c_uint32),
        ('minSgprAllocation', ctypes.c_uint32),
        ('maxSgprAllocation', ctypes.c_uint32),
        ('sgprAllocationGranularity', ctypes.c_uint32),
        ('vgprsPerSimd', ctypes.c_uint32),
        ('minVgprAllocation', ctypes.c_uint32),
        ('maxVgprAllocation', ctypes.c_uint32),
        ('vgprAllocationGranularity', ctypes.c_uint32),
    ]
