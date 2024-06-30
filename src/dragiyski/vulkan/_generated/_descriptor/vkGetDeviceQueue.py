from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetDeviceQueue'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'queueFamilyIndex', 'queueIndex', 'pQueue']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'queueFamilyIndex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'queueIndex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pQueue': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
