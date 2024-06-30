from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkUninitializePerformanceApiINTEL'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
