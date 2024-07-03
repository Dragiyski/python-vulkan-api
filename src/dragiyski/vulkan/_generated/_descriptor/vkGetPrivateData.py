from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetPrivateData'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'objectType', 'objectHandle', 'privateDataSlot', 'pData']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'objectType': {
        'type': CIntType('c_int'),
        'is_string': False,
        'output': False,
    },
    'objectHandle': {
        'type': CIntType('c_uint64'),
        'is_string': False,
        'output': False,
    },
    'privateDataSlot': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pData': {
        'type': CPointerType(CIntType('c_uint64')),
        'is_string': False,
        'output': True,
    },
}
_return_type_ = CVoidType()
