from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdSetDepthBias'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'depthBiasConstantFactor', 'depthBiasClamp', 'depthBiasSlopeFactor']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'depthBiasConstantFactor': {
        'type': CFloatType('c_float'),
        'is_string': False,
        'output': False,
    },
    'depthBiasClamp': {
        'type': CFloatType('c_float'),
        'is_string': False,
        'output': False,
    },
    'depthBiasSlopeFactor': {
        'type': CFloatType('c_float'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
