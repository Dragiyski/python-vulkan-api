from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCreateSharedSwapchainsKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'swapchainCount', 'pCreateInfos', 'pAllocator', 'pSwapchains']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'swapchainCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pCreateInfos': {
        'type': CPointerType(CComplexType('VkSwapchainCreateInfoKHR')),
        'is_string': False,
        'length': [['swapchainCount']],
        'output': False,
    },
    'pAllocator': {
        'type': CPointerType(CComplexType('VkAllocationCallbacks')),
        'is_string': False,
        'output': False,
    },
    'pSwapchains': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
        'length': [['swapchainCount']],
        'output': True,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_INCOMPATIBLE_DISPLAY_KHR', 'VK_ERROR_OUT_OF_HOST_MEMORY', 'VK_ERROR_OUT_OF_DEVICE_MEMORY', 'VK_ERROR_DEVICE_LOST', 'VK_ERROR_SURFACE_LOST_KHR'}
