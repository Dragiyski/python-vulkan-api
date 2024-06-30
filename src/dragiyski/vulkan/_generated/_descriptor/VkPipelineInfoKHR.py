from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPipelineInfoKHR'
_member_list_ = ['sType', 'pNext', 'pipeline']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PIPELINE_INFO_KHR',
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
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkGetPipelineExecutablePropertiesKHR',
    'vkGetPipelinePropertiesEXT',
}
_output_of_ = set()
