from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdSetCheckpointNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pCheckpointMarker']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pCheckpointMarker': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
