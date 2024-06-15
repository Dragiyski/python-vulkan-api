import ctypes, sys

class VkTraceRaysIndirectCommand2KHR(ctypes.Structure):
    _fields_ = [
        ('raygenShaderRecordAddress', ctypes.c_uint64),
        ('raygenShaderRecordSize', ctypes.c_uint64),
        ('missShaderBindingTableAddress', ctypes.c_uint64),
        ('missShaderBindingTableSize', ctypes.c_uint64),
        ('missShaderBindingTableStride', ctypes.c_uint64),
        ('hitShaderBindingTableAddress', ctypes.c_uint64),
        ('hitShaderBindingTableSize', ctypes.c_uint64),
        ('hitShaderBindingTableStride', ctypes.c_uint64),
        ('callableShaderBindingTableAddress', ctypes.c_uint64),
        ('callableShaderBindingTableSize', ctypes.c_uint64),
        ('callableShaderBindingTableStride', ctypes.c_uint64),
        ('width', ctypes.c_uint32),
        ('height', ctypes.c_uint32),
        ('depth', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkTraceRaysIndirectCommand2KHR
