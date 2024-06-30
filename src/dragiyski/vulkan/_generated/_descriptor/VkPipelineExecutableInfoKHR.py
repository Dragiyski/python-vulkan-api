from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPipelineExecutableInfoKHR'
_member_list_ = ['sType', 'pNext', 'pipeline', 'executableIndex']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PIPELINE_EXECUTABLE_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pipeline': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'executableIndex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkGetPipelineExecutableInternalRepresentationsKHR',
    'vkGetPipelineExecutableStatisticsKHR',
}
_output_of_ = set()
