from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdUpdateBuffer'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'dstBuffer', 'dstOffset', 'dataSize', 'pData']
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
    'dataSize': {
        'type': CIntType('c_uint64'),
        'is_string': False,
        'output': False,
    },
    'pData': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'length': [['dataSize']],
        'output': False,
    },
}
_return_type_ = CVoidType()
