from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkRegisterDeviceEventEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pDeviceEventInfo', 'pAllocator', 'pFence']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pDeviceEventInfo': {
        'type': CPointerType(CComplexType('VkDeviceEventInfoEXT')),
        'is_string': False,
    },
    'pAllocator': {
        'type': CPointerType(CComplexType('VkAllocationCallbacks')),
        'is_string': False,
    },
    'pFence': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_OUT_OF_HOST_MEMORY'}
