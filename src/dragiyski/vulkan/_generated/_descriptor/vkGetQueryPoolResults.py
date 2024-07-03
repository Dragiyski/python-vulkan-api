from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetQueryPoolResults'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'queryPool', 'firstQuery', 'queryCount', 'dataSize', 'pData', 'stride', 'flags']
_argument_info_ = {
    'device': {
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
    'dataSize': {
        'type': CIntType('c_size_t'),
        'is_string': False,
        'output': False,
    },
    'pData': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'length': [['dataSize']],
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
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_NOT_READY', 'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_OUT_OF_HOST_MEMORY', 'VK_ERROR_OUT_OF_DEVICE_MEMORY', 'VK_ERROR_DEVICE_LOST'}
