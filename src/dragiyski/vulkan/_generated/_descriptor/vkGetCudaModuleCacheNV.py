from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetCudaModuleCacheNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'module', 'pCacheSize', 'pCacheData']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'module': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pCacheSize': {
        'type': CPointerType(CIntType('c_size_t')),
        'is_string': False,
    },
    'pCacheData': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'length': [['pCacheSize']],
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS', 'VK_INCOMPLETE'}
_error_code_list_ = {'VK_ERROR_INITIALIZATION_FAILED'}
