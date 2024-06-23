import ctypes

class CType(ctypes.Structure):
    pass

from .VkPipelineExecutableStatisticValueKHR import CType as VkPipelineExecutableStatisticValueKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('name', ctypes.ARRAY(ctypes.c_char, 256)),
    ('description', ctypes.ARRAY(ctypes.c_char, 256)),
    ('format', ctypes.c_int),
    ('value', VkPipelineExecutableStatisticValueKHR),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkPipelineExecutableStatisticValueKHR',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetPipelineExecutableStatisticsKHR',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PIPELINE_EXECUTABLE_STATISTIC_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'name': {'python_name': ['name'], 'len': [['null-terminated']]},
        'description': {'python_name': ['description'], 'len': [['null-terminated']]},
        'format': {'python_name': ['format'], 'type': 'VkPipelineExecutableStatisticFormatKHR'},
        'value': {'python_name': ['value'], 'type': 'VkPipelineExecutableStatisticValueKHR'},
    }
}
