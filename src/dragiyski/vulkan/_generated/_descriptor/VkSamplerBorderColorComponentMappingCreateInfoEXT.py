from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSamplerBorderColorComponentMappingCreateInfoEXT'
_member_list_ = ['sType', 'pNext', 'components', 'srgb']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_SAMPLER_BORDER_COLOR_COMPONENT_MAPPING_CREATE_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'components': {
        'type': CComplexType('VkComponentMapping'),
        'type_name': 'VkComponentMapping',
        'structure': 'VkComponentMapping',
        'is_string': False,
    },
    'srgb': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = {
    'VkSamplerCreateInfo',
}
_extended_by_ = set()
_includes_ = {
    'VkComponentMapping',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
