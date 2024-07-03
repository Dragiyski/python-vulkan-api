from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdCopyQueryPoolResults'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'queryPool', 'firstQuery', 'queryCount', 'dstBuffer', 'dstOffset', 'stride', 'flags']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'queryPool': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'firstQuery': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'queryCount': {
        'type': CIntType('c_uint32'),
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
    'stride': {
        'type': CIntType('c_uint64'),
        'is_string': False,
        'output': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
