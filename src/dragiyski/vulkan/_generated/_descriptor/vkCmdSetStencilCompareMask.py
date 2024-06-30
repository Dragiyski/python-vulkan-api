from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdSetStencilCompareMask'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'faceMask', 'compareMask']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'faceMask': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'compareMask': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
