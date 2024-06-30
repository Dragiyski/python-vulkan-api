from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCopyMemoryToImageEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pCopyMemoryToImageInfo']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pCopyMemoryToImageInfo': {
        'type': CPointerType(CComplexType('VkCopyMemoryToImageInfoEXT')),
        'is_string': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_INITIALIZATION_FAILED', 'VK_ERROR_MEMORY_MAP_FAILED', 'VK_ERROR_OUT_OF_DEVICE_MEMORY', 'VK_ERROR_OUT_OF_HOST_MEMORY'}
