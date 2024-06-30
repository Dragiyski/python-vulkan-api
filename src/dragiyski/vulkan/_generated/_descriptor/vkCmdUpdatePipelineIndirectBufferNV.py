from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdUpdatePipelineIndirectBufferNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pipelineBindPoint', 'pipeline']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pipelineBindPoint': {
        'type': CIntType('c_int'),
        'is_string': False,
    },
    'pipeline': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
