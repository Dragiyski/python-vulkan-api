from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPipelineViewportSwizzleStateCreateInfoNV'
_member_list_ = ['sType', 'pNext', 'flags', 'viewportCount', 'pViewportSwizzles']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_SWIZZLE_STATE_CREATE_INFO_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkPipelineViewportSwizzleStateCreateFlagsNV',
        'enum': 'VkPipelineViewportSwizzleStateCreateFlagsNV',
        'is_string': False,
    },
    'viewportCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pViewportSwizzles': {
        'type': CPointerType(CComplexType('VkViewportSwizzleNV')),
        'type_name': 'VkViewportSwizzleNV',
        'structure': 'VkViewportSwizzleNV',
        'length': [['viewportCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkPipelineViewportStateCreateInfo',
}
_extended_by_ = set()
_includes_ = {
    'VkViewportSwizzleNV',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
