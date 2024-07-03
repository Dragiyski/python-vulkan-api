from ..._ctypes import *

category = 'callback'
_name_ = 'vkAllocationFunction'
_constructor_ = 'VKAPI_PTR'
_argument_list_ = ['pUserData', 'size', 'alignment', 'allocationScope']
_argument_info_ = {
    'pUserData': {
        'type': CIntType('c_void_p'),
    },
    'size': {
        'type': CIntType('c_size_t'),
    },
    'alignment': {
        'type': CIntType('c_size_t'),
    },
    'allocationScope': {
        'type': CIntType('c_int'),
    },
}
_return_type_ = CIntType('c_void_p')
