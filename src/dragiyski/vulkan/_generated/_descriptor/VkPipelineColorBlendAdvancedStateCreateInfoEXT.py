from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPipelineColorBlendAdvancedStateCreateInfoEXT'
_member_list_ = ['sType', 'pNext', 'srcPremultiplied', 'dstPremultiplied', 'blendOverlap']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PIPELINE_COLOR_BLEND_ADVANCED_STATE_CREATE_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'srcPremultiplied': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'dstPremultiplied': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'blendOverlap': {
        'type': CIntType('c_int'),
        'type_name': 'VkBlendOverlapEXT',
        'enum': 'VkBlendOverlapEXT',
        'is_string': False,
    },
}
_extends_ = {
    'VkPipelineColorBlendStateCreateInfo',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
