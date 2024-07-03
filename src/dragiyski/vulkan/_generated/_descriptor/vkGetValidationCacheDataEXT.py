from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetValidationCacheDataEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'validationCache', 'pDataSize', 'pData']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'validationCache': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pDataSize': {
        'type': CPointerType(CIntType('c_size_t')),
        'is_string': False,
        'output': True,
    },
    'pData': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'length': [['pDataSize']],
        'output': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS', 'VK_INCOMPLETE'}
_error_code_list_ = {'VK_ERROR_OUT_OF_HOST_MEMORY', 'VK_ERROR_OUT_OF_DEVICE_MEMORY'}
