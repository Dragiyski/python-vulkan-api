import ctypes, sys

class VkPhysicalDeviceMeshShaderPropertiesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxDrawMeshTasksCount', ctypes.c_uint32),
        ('maxTaskWorkGroupInvocations', ctypes.c_uint32),
        ('maxTaskWorkGroupSize', ctypes.ARRAY(ctypes.c_uint32, 3)),
        ('maxTaskTotalMemorySize', ctypes.c_uint32),
        ('maxTaskOutputCount', ctypes.c_uint32),
        ('maxMeshWorkGroupInvocations', ctypes.c_uint32),
        ('maxMeshWorkGroupSize', ctypes.ARRAY(ctypes.c_uint32, 3)),
        ('maxMeshTotalMemorySize', ctypes.c_uint32),
        ('maxMeshOutputVertices', ctypes.c_uint32),
        ('maxMeshOutputPrimitives', ctypes.c_uint32),
        ('maxMeshMultiviewViewCount', ctypes.c_uint32),
        ('meshOutputPerVertexGranularity', ctypes.c_uint32),
        ('meshOutputPerPrimitiveGranularity', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceMeshShaderPropertiesNV
