from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetSwapchainGrallocUsageANDROID'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'format', 'imageUsage', 'grallocUsage']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'format': {
        'type': CIntType('c_int'),
        'is_string': False,
    },
    'imageUsage': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'grallocUsage': {
        'type': CPointerType(CIntType('c_int')),
        'is_string': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = set()
_error_code_list_ = set()
