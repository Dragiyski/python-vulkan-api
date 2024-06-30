from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCreateDebugReportCallbackEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['instance', 'pCreateInfo', 'pAllocator', 'pCallback']
_argument_info_ = {
    'instance': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pCreateInfo': {
        'type': CPointerType(CComplexType('VkDebugReportCallbackCreateInfoEXT')),
        'is_string': False,
    },
    'pAllocator': {
        'type': CPointerType(CComplexType('VkAllocationCallbacks')),
        'is_string': False,
    },
    'pCallback': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_OUT_OF_HOST_MEMORY'}
