from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCopyMicromapEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'deferredOperation', 'pInfo']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'deferredOperation': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pInfo': {
        'type': CPointerType(CComplexType('VkCopyMicromapInfoEXT')),
        'is_string': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS', 'VK_OPERATION_NOT_DEFERRED_KHR', 'VK_OPERATION_DEFERRED_KHR'}
_error_code_list_ = {'VK_ERROR_OUT_OF_DEVICE_MEMORY', 'VK_ERROR_OUT_OF_HOST_MEMORY'}
