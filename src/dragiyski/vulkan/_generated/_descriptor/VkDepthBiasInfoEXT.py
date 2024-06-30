from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDepthBiasInfoEXT'
_member_list_ = ['sType', 'pNext', 'depthBiasConstantFactor', 'depthBiasClamp', 'depthBiasSlopeFactor']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_DEPTH_BIAS_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'depthBiasConstantFactor': {
        'type': CFloatType('c_float'),
        'is_string': False,
    },
    'depthBiasClamp': {
        'type': CFloatType('c_float'),
        'is_string': False,
    },
    'depthBiasSlopeFactor': {
        'type': CFloatType('c_float'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkDepthBiasRepresentationInfoEXT',
}
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkCmdSetDepthBias2EXT',
}
_output_of_ = set()
