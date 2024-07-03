from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdBindIndexBuffer2KHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'buffer', 'offset', 'size', 'indexType']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'buffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'offset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
        'output': False,
    },
    'size': {
        'type': CIntType('c_uint64'),
        'is_string': False,
        'output': False,
    },
    'indexType': {
        'type': CIntType('c_int'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
