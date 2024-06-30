from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkImportSemaphoreFdKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pImportSemaphoreFdInfo']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pImportSemaphoreFdInfo': {
        'type': CPointerType(CComplexType('VkImportSemaphoreFdInfoKHR')),
        'is_string': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_INVALID_EXTERNAL_HANDLE', 'VK_ERROR_OUT_OF_HOST_MEMORY'}
