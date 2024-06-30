from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCreateDisplayModeKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'display', 'pCreateInfo', 'pAllocator', 'pMode']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'display': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pCreateInfo': {
        'type': CPointerType(CComplexType('VkDisplayModeCreateInfoKHR')),
        'is_string': False,
    },
    'pAllocator': {
        'type': CPointerType(CComplexType('VkAllocationCallbacks')),
        'is_string': False,
    },
    'pMode': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_INITIALIZATION_FAILED', 'VK_ERROR_OUT_OF_DEVICE_MEMORY', 'VK_ERROR_OUT_OF_HOST_MEMORY'}
