from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdUpdateBuffer'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'dstBuffer', 'dstOffset', 'dataSize', 'pData']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
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
    'dataSize': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'pData': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'length': [['dataSize']],
    },
}
_return_type_ = CVoidType()
