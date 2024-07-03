from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdBindPipelineShaderGroupNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pipelineBindPoint', 'pipeline', 'groupIndex']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pipelineBindPoint': {
        'type': CIntType('c_int'),
        'is_string': False,
        'output': False,
    },
    'pipeline': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'groupIndex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
