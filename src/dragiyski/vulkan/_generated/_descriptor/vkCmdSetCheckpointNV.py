from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdSetCheckpointNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pCheckpointMarker']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pCheckpointMarker': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
