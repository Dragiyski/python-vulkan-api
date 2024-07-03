from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetSwapchainGrallocUsageANDROID'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'format', 'imageUsage', 'grallocUsage']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'format': {
        'type': CIntType('c_int'),
        'is_string': False,
        'output': False,
    },
    'imageUsage': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'grallocUsage': {
        'type': CPointerType(CIntType('c_int')),
        'is_string': False,
        'output': True,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = set()
_error_code_list_ = set()
