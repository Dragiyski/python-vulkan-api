from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetSwapchainCounterEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'swapchain', 'counter', 'pCounterValue']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'swapchain': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'counter': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pCounterValue': {
        'type': CPointerType(CIntType('c_uint64')),
        'is_string': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_DEVICE_LOST', 'VK_ERROR_OUT_OF_HOST_MEMORY', 'VK_ERROR_OUT_OF_DATE_KHR'}
