from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetRandROutputDisplayEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'dpy', 'rrOutput', 'pDisplay']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'dpy': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'rrOutput': {
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
_error_code_list_ = {'VK_ERROR_OUT_OF_HOST_MEMORY'}
