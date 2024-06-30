from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdCopyQueryPoolResults'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'queryPool', 'firstQuery', 'queryCount', 'dstBuffer', 'dstOffset', 'stride', 'flags']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'queryPool': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'firstQuery': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'queryCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'dstBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'dstOffset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'stride': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
