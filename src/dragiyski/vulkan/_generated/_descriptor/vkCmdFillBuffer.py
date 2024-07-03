from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdFillBuffer'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'dstBuffer', 'dstOffset', 'size', 'data']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'dstBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'dstOffset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
        'output': False,
    },
    'size': {
        'type': CIntType('c_uint64'),
        'is_string': False,
        'output': False,
    },
    'data': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
