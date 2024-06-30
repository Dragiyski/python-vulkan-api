from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPushConstantRange'
_member_list_ = ['stageFlags', 'offset', 'size']
_member_info_ = {
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
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkPipelineLayoutCreateInfo',
    'VkShaderCreateInfoEXT',
}
_input_of_ = set()
_output_of_ = set()
