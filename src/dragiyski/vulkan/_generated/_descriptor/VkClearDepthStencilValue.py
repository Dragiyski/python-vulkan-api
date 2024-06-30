from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkClearDepthStencilValue'
_member_list_ = ['depth', 'stencil']
_member_info_ = {
    'depth': {
        'type': CFloatType('c_float'),
        'is_string': False,
    },
    'stencil': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkClearValue',
}
_input_of_ = {
    'vkCmdClearDepthStencilImage',
}
_output_of_ = set()
