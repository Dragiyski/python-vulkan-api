from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetPrivateData'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'objectType', 'objectHandle', 'privateDataSlot', 'pData']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'objectType': {
        'type': CIntType('c_int'),
        'is_string': False,
    },
    'objectHandle': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'privateDataSlot': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pData': {
        'type': CPointerType(CIntType('c_uint64')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
