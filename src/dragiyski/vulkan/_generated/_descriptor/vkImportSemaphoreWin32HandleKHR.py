from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkImportSemaphoreWin32HandleKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pImportSemaphoreWin32HandleInfo']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pImportSemaphoreWin32HandleInfo': {
        'type': CPointerType(CComplexType('VkImportSemaphoreWin32HandleInfoKHR')),
        'is_string': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_INVALID_EXTERNAL_HANDLE', 'VK_ERROR_OUT_OF_HOST_MEMORY'}
