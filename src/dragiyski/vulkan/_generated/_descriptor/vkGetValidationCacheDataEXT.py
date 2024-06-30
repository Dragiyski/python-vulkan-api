from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetValidationCacheDataEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'validationCache', 'pDataSize', 'pData']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'validationCache': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pDataSize': {
        'type': CPointerType(CIntType('c_size_t')),
        'is_string': False,
    },
    'pData': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'length': [['pDataSize']],
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS', 'VK_INCOMPLETE'}
_error_code_list_ = {'VK_ERROR_OUT_OF_DEVICE_MEMORY', 'VK_ERROR_OUT_OF_HOST_MEMORY'}
