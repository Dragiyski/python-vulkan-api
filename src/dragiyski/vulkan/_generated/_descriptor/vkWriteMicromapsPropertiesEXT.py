from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkWriteMicromapsPropertiesEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'micromapCount', 'pMicromaps', 'queryType', 'dataSize', 'pData', 'stride']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'micromapCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pMicromaps': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
        'length': [['micromapCount']],
        'output': False,
    },
    'queryType': {
        'type': CIntType('c_int'),
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
        'type': CIntType('c_size_t'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_OUT_OF_HOST_MEMORY', 'VK_ERROR_OUT_OF_DEVICE_MEMORY'}
