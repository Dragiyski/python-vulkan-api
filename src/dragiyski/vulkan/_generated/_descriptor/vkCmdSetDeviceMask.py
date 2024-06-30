from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdSetDeviceMask'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'deviceMask']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'deviceMask': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
