import ctypes

class CType(ctypes.Structure):
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

descriptor = {
    'extends': {
        'VkPhysicalDeviceProperties2',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MESH_SHADER_PROPERTIES_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'maxDrawMeshTasksCount': {'python_name': ['max', 'draw', 'mesh', 'tasks', 'count']},
        'maxTaskWorkGroupInvocations': {'python_name': ['max', 'task', 'work', 'group', 'invocations']},
        'maxTaskWorkGroupSize': {'python_name': ['max', 'task', 'work', 'group', 'size']},
        'maxTaskTotalMemorySize': {'python_name': ['max', 'task', 'total', 'memory', 'size']},
        'maxTaskOutputCount': {'python_name': ['max', 'task', 'output', 'count']},
        'maxMeshWorkGroupInvocations': {'python_name': ['max', 'mesh', 'work', 'group', 'invocations']},
        'maxMeshWorkGroupSize': {'python_name': ['max', 'mesh', 'work', 'group', 'size']},
        'maxMeshTotalMemorySize': {'python_name': ['max', 'mesh', 'total', 'memory', 'size']},
        'maxMeshOutputVertices': {'python_name': ['max', 'mesh', 'output', 'vertices']},
        'maxMeshOutputPrimitives': {'python_name': ['max', 'mesh', 'output', 'primitives']},
        'maxMeshMultiviewViewCount': {'python_name': ['max', 'mesh', 'multiview', 'view', 'count']},
        'meshOutputPerVertexGranularity': {'python_name': ['mesh', 'output', 'per', 'vertex', 'granularity']},
        'meshOutputPerPrimitiveGranularity': {'python_name': ['mesh', 'output', 'per', 'primitive', 'granularity']},
    }
}
