from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkColorBlendAdvancedEXT'
_member_list_ = ['advancedBlendOp', 'srcPremultiplied', 'dstPremultiplied', 'blendOverlap', 'clampResults']
_member_info_ = {
    'advancedBlendOp': {
        'type': CIntType('c_int'),
        'type_name': 'VkBlendOp',
        'enum': 'VkBlendOp',
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
    'clampResults': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkCmdSetColorBlendAdvancedEXT',
}
_output_of_ = set()
