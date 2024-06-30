from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPushConstantsInfoKHR'
_member_list_ = ['sType', 'pNext', 'layout', 'stageFlags', 'offset', 'size', 'pValues']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PUSH_CONSTANTS_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'layout': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'stageFlags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkShaderStageFlags',
        'enum': 'VkShaderStageFlags',
        'is_string': False,
    },
    'offset': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'size': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pValues': {
        'type': CIntType('c_void_p'),
        'length': [['size']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkPipelineLayoutCreateInfo',
}
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkCmdPushConstants2KHR',
}
_output_of_ = set()
