import ctypes, sys

class VkPhysicalDeviceMeshShaderPropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxTaskWorkGroupTotalCount', ctypes.c_uint32),
        ('maxTaskWorkGroupCount', ctypes.ARRAY(ctypes.c_uint32, 3)),
        ('maxTaskWorkGroupInvocations', ctypes.c_uint32),
        ('maxTaskWorkGroupSize', ctypes.ARRAY(ctypes.c_uint32, 3)),
        ('maxTaskPayloadSize', ctypes.c_uint32),
        ('maxTaskSharedMemorySize', ctypes.c_uint32),
        ('maxTaskPayloadAndSharedMemorySize', ctypes.c_uint32),
        ('maxMeshWorkGroupTotalCount', ctypes.c_uint32),
        ('maxMeshWorkGroupCount', ctypes.ARRAY(ctypes.c_uint32, 3)),
        ('maxMeshWorkGroupInvocations', ctypes.c_uint32),
        ('maxMeshWorkGroupSize', ctypes.ARRAY(ctypes.c_uint32, 3)),
        ('maxMeshSharedMemorySize', ctypes.c_uint32),
        ('maxMeshPayloadAndSharedMemorySize', ctypes.c_uint32),
        ('maxMeshOutputMemorySize', ctypes.c_uint32),
        ('maxMeshPayloadAndOutputMemorySize', ctypes.c_uint32),
        ('maxMeshOutputComponents', ctypes.c_uint32),
        ('maxMeshOutputVertices', ctypes.c_uint32),
        ('maxMeshOutputPrimitives', ctypes.c_uint32),
        ('maxMeshOutputLayers', ctypes.c_uint32),
        ('maxMeshMultiviewViewCount', ctypes.c_uint32),
        ('meshOutputPerVertexGranularity', ctypes.c_uint32),
        ('meshOutputPerPrimitiveGranularity', ctypes.c_uint32),
        ('maxPreferredTaskWorkGroupInvocations', ctypes.c_uint32),
        ('maxPreferredMeshWorkGroupInvocations', ctypes.c_uint32),
        ('prefersLocalInvocationVertexOutput', ctypes.c_uint32),
        ('prefersLocalInvocationPrimitiveOutput', ctypes.c_uint32),
        ('prefersCompactVertexOutput', ctypes.c_uint32),
        ('prefersCompactPrimitiveOutput', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceMeshShaderPropertiesEXT