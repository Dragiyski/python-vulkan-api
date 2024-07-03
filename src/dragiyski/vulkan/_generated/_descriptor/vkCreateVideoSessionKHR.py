from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCreateVideoSessionKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pCreateInfo', 'pAllocator', 'pVideoSession']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pCreateInfo': {
        'type': CPointerType(CComplexType('VkVideoSessionCreateInfoKHR')),
        'is_string': False,
        'output': False,
    },
    'pAllocator': {
        'type': CPointerType(CComplexType('VkAllocationCallbacks')),
        'is_string': False,
        'output': False,
    },
    'pVideoSession': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
        'output': True,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_INVALID_VIDEO_STD_PARAMETERS_KHR', 'VK_ERROR_OUT_OF_HOST_MEMORY', 'VK_ERROR_OUT_OF_DEVICE_MEMORY', 'VK_ERROR_VIDEO_STD_VERSION_NOT_SUPPORTED_KHR', 'VK_ERROR_INITIALIZATION_FAILED'}
