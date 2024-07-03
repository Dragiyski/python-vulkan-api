from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCreateInstance'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['pCreateInfo', 'pAllocator', 'pInstance']
_argument_info_ = {
    'pCreateInfo': {
        'type': CPointerType(CComplexType('VkInstanceCreateInfo')),
        'is_string': False,
        'output': False,
    },
    'pAllocator': {
        'type': CPointerType(CComplexType('VkAllocationCallbacks')),
        'is_string': False,
        'output': False,
    },
    'pInstance': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
        'output': True,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_LAYER_NOT_PRESENT', 'VK_ERROR_OUT_OF_HOST_MEMORY', 'VK_ERROR_INCOMPATIBLE_DRIVER', 'VK_ERROR_OUT_OF_DEVICE_MEMORY', 'VK_ERROR_EXTENSION_NOT_PRESENT', 'VK_ERROR_INITIALIZATION_FAILED'}
