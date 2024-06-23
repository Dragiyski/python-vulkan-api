import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pipeline', ctypes.c_void_p),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkGetPipelineExecutablePropertiesKHR',
        'vkGetPipelinePropertiesEXT',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PIPELINE_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'pipeline': {'python_name': ['pipeline']},
    }
}
