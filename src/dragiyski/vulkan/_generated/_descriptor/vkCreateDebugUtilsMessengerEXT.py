from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCreateDebugUtilsMessengerEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['instance', 'pCreateInfo', 'pAllocator', 'pMessenger']
_argument_info_ = {
    'instance': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pCreateInfo': {
        'type': CPointerType(CComplexType('VkDebugUtilsMessengerCreateInfoEXT')),
        'is_string': False,
        'output': False,
    },
    'pAllocator': {
        'type': CPointerType(CComplexType('VkAllocationCallbacks')),
        'is_string': False,
        'output': False,
    },
    'pMessenger': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
        'output': True,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_OUT_OF_HOST_MEMORY'}
