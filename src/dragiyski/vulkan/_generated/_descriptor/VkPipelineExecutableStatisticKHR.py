from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPipelineExecutableStatisticKHR'
_member_list_ = ['sType', 'pNext', 'name', 'description', 'format', 'value']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PIPELINE_EXECUTABLE_STATISTIC_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'name': {
        'type': CArrayType(CCharType('c_char'), 256),
        'length': [],
        'is_string': True,
    },
    'description': {
        'type': CArrayType(CCharType('c_char'), 256),
        'length': [],
        'is_string': True,
    },
    'format': {
        'type': CIntType('c_int'),
        'type_name': 'VkPipelineExecutableStatisticFormatKHR',
        'enum': 'VkPipelineExecutableStatisticFormatKHR',
        'is_string': False,
    },
    'value': {
        'type': CComplexType('VkPipelineExecutableStatisticValueKHR'),
        'type_name': 'VkPipelineExecutableStatisticValueKHR',
        'union': 'VkPipelineExecutableStatisticValueKHR',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkPipelineExecutableStatisticValueKHR',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = {
    'vkGetPipelineExecutableStatisticsKHR',
}
