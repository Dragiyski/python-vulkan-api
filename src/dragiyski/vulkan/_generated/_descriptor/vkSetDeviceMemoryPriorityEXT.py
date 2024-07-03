from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkSetDeviceMemoryPriorityEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'memory', 'priority']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'memory': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'priority': {
        'type': CFloatType('c_float'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
