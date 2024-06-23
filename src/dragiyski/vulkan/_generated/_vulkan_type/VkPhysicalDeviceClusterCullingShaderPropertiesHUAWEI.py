import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxWorkGroupCount', ctypes.ARRAY(ctypes.c_uint32, 3)),
        ('maxWorkGroupSize', ctypes.ARRAY(ctypes.c_uint32, 3)),
        ('maxOutputClusterCount', ctypes.c_uint32),
        ('indirectBufferOffsetAlignment', ctypes.c_uint64),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_CLUSTER_CULLING_SHADER_PROPERTIES_HUAWEI', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'maxWorkGroupCount': {'python_name': ['max', 'work', 'group', 'count']},
        'maxWorkGroupSize': {'python_name': ['max', 'work', 'group', 'size']},
        'maxOutputClusterCount': {'python_name': ['max', 'output', 'cluster', 'count']},
        'indirectBufferOffsetAlignment': {'python_name': ['indirect', 'buffer', 'offset', 'alignment']},
    }
}
