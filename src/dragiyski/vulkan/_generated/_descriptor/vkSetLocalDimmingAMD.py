from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkSetLocalDimmingAMD'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'swapChain', 'localDimmingEnable']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'swapChain': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'localDimmingEnable': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
