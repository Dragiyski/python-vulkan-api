from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkWriteMicromapsPropertiesEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'micromapCount', 'pMicromaps', 'queryType', 'dataSize', 'pData', 'stride']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'micromapCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pMicromaps': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
        'length': [['micromapCount']],
    },
    'queryType': {
        'type': CIntType('c_int'),
        'is_string': False,
    },
    'dataSize': {
        'type': CIntType('c_size_t'),
        'is_string': False,
    },
    'pData': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'length': [['dataSize']],
    },
    'stride': {
        'type': CIntType('c_size_t'),
        'is_string': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_OUT_OF_DEVICE_MEMORY', 'VK_ERROR_OUT_OF_HOST_MEMORY'}
