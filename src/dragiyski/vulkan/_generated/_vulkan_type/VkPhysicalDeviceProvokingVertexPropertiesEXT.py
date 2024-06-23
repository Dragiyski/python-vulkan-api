import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('provokingVertexModePerPipeline', ctypes.c_uint32),
        ('transformFeedbackPreservesTriangleFanProvokingVertex', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PROVOKING_VERTEX_PROPERTIES_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'provokingVertexModePerPipeline': {'python_name': ['provoking', 'vertex', 'mode', 'per', 'pipeline']},
        'transformFeedbackPreservesTriangleFanProvokingVertex': {'python_name': ['transform', 'feedback', 'preserves', 'triangle', 'fan', 'provoking', 'vertex']},
    }
}
