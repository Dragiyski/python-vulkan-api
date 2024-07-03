from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkRegisterDeviceEventEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pDeviceEventInfo', 'pAllocator', 'pFence']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pDeviceEventInfo': {
        'type': CPointerType(CComplexType('VkDeviceEventInfoEXT')),
        'is_string': False,
        'output': False,
    },
    'pAllocator': {
        'type': CPointerType(CComplexType('VkAllocationCallbacks')),
        'is_string': False,
        'output': False,
    },
    'pFence': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
        'output': True,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_OUT_OF_HOST_MEMORY'}
