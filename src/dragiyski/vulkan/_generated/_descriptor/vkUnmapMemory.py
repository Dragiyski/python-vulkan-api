from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkUnmapMemory'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'memory']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'memory': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
