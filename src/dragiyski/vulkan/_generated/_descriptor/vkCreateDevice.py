from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCreateDevice'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'pCreateInfo', 'pAllocator', 'pDevice']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pCreateInfo': {
        'type': CPointerType(CComplexType('VkDeviceCreateInfo')),
        'is_string': False,
    },
    'pAllocator': {
        'type': CPointerType(CComplexType('VkAllocationCallbacks')),
        'is_string': False,
    },
    'pDevice': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_EXTENSION_NOT_PRESENT', 'VK_ERROR_DEVICE_LOST', 'VK_ERROR_OUT_OF_HOST_MEMORY', 'VK_ERROR_FEATURE_NOT_PRESENT', 'VK_ERROR_TOO_MANY_OBJECTS', 'VK_ERROR_INITIALIZATION_FAILED', 'VK_ERROR_OUT_OF_DEVICE_MEMORY'}
