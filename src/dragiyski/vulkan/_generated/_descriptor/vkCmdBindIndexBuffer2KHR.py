from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdBindIndexBuffer2KHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'buffer', 'offset', 'size', 'indexType']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'buffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'offset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'size': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'indexType': {
        'type': CIntType('c_int'),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
