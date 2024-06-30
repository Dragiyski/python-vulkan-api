from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdSetStencilReference'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'faceMask', 'reference']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'faceMask': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'reference': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
