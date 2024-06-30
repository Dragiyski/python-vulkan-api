from ..._ctypes import *

_category_ = 'union'
_name_ = 'VkClearColorValue'
_member_list_ = ['float32', 'int32', 'uint32']
_member_info_ = {
    'float32': {
        'type': CArrayType(CFloatType('c_float'), 4),
        'is_string': False,
    },
    'int32': {
        'type': CArrayType(CIntType('c_int32'), 4),
        'is_string': False,
    },
    'uint32': {
        'type': CArrayType(CIntType('c_uint32'), 4),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkClearValue',
    'VkSamplerCustomBorderColorCreateInfoEXT',
}
_input_of_ = {
    'vkCmdClearColorImage',
}
_output_of_ = set()
