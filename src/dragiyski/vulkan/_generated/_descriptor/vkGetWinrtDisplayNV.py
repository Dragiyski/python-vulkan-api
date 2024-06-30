from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetWinrtDisplayNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'deviceRelativeId', 'pDisplay']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'deviceRelativeId': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pDisplay': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_INITIALIZATION_FAILED', 'VK_ERROR_DEVICE_LOST', 'VK_ERROR_OUT_OF_HOST_MEMORY'}
