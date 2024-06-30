from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSamplerCustomBorderColorCreateInfoEXT'
_member_list_ = ['sType', 'pNext', 'customBorderColor', 'format']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_SAMPLER_CUSTOM_BORDER_COLOR_CREATE_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'customBorderColor': {
        'type': CComplexType('VkClearColorValue'),
        'type_name': 'VkClearColorValue',
        'union': 'VkClearColorValue',
        'is_string': False,
    },
    'format': {
        'type': CIntType('c_int'),
        'type_name': 'VkFormat',
        'enum': 'VkFormat',
        'is_string': False,
    },
}
_extends_ = {
    'VkSamplerCreateInfo',
}
_extended_by_ = set()
_includes_ = {
    'VkClearColorValue',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
