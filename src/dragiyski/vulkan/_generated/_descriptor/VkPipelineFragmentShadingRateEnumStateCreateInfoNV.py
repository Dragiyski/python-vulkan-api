from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPipelineFragmentShadingRateEnumStateCreateInfoNV'
_member_list_ = ['sType', 'pNext', 'shadingRateType', 'shadingRate', 'combinerOps']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PIPELINE_FRAGMENT_SHADING_RATE_ENUM_STATE_CREATE_INFO_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'shadingRateType': {
        'type': CIntType('c_int'),
        'type_name': 'VkFragmentShadingRateTypeNV',
        'enum': 'VkFragmentShadingRateTypeNV',
        'is_string': False,
    },
    'shadingRate': {
        'type': CIntType('c_int'),
        'type_name': 'VkFragmentShadingRateNV',
        'enum': 'VkFragmentShadingRateNV',
        'is_string': False,
    },
    'combinerOps': {
        'type': CArrayType(CIntType('c_int'), 2),
        'type_name': 'VkFragmentShadingRateCombinerOpKHR',
        'enum': 'VkFragmentShadingRateCombinerOpKHR',
        'is_string': False,
    },
}
_extends_ = {
    'VkGraphicsPipelineCreateInfo',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
