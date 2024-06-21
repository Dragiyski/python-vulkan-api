import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('storageBuffer16BitAccess', ctypes.c_uint32),
        ('uniformAndStorageBuffer16BitAccess', ctypes.c_uint32),
        ('storagePushConstant16', ctypes.c_uint32),
        ('storageInputOutput16', ctypes.c_uint32),
        ('multiview', ctypes.c_uint32),
        ('multiviewGeometryShader', ctypes.c_uint32),
        ('multiviewTessellationShader', ctypes.c_uint32),
        ('variablePointersStorageBuffer', ctypes.c_uint32),
        ('variablePointers', ctypes.c_uint32),
        ('protectedMemory', ctypes.c_uint32),
        ('samplerYcbcrConversion', ctypes.c_uint32),
        ('shaderDrawParameters', ctypes.c_uint32),
    ]
