from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkSetLocalDimmingAMD'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'swapChain', 'localDimmingEnable']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'swapChain': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'localDimmingEnable': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
