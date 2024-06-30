from ..._ctypes import *

_category_ = 'callback'
_name_ = 'vkInternalAllocationNotification'
_constructor_ = 'VKAPI_PTR'
_argument_list_ = ['pUserData', 'size', 'allocationType', 'allocationScope']
_argument_info_ = {
    'pUserData': {
        'type': CIntType('c_void_p'),
    },
    'size': {
        'type': CIntType('c_size_t'),
    },
    'allocationType': {
        'type': CIntType('c_int'),
    },
    'allocationScope': {
        'type': CIntType('c_int'),
    },
}
_return_type_ = CVoidType()
