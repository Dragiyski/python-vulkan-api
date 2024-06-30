from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdSetExclusiveScissorEnableNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'firstExclusiveScissor', 'exclusiveScissorCount', 'pExclusiveScissorEnables']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'firstExclusiveScissor': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'exclusiveScissorCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pExclusiveScissorEnables': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
        'length': [['exclusiveScissorCount']],
    },
}
_return_type_ = CVoidType()
