from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetDeviceQueue'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'queueFamilyIndex', 'queueIndex', 'pQueue']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'queueFamilyIndex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'queueIndex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pQueue': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
        'output': True,
    },
}
_return_type_ = CVoidType()
