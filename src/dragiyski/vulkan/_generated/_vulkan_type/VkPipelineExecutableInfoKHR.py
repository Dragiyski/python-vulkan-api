import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pipeline', ctypes.c_void_p),
        ('executableIndex', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkGetPipelineExecutableInternalRepresentationsKHR',
        'vkGetPipelineExecutableStatisticsKHR',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PIPELINE_EXECUTABLE_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'pipeline': {'python_name': ['pipeline']},
        'executableIndex': {'python_name': ['executable', 'index']},
    }
}
