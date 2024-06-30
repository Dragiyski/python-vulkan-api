from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdSetDepthBias'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'depthBiasConstantFactor', 'depthBiasClamp', 'depthBiasSlopeFactor']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'depthBiasConstantFactor': {
        'type': CFloatType('c_float'),
        'is_string': False,
    },
    'depthBiasClamp': {
        'type': CFloatType('c_float'),
        'is_string': False,
    },
    'depthBiasSlopeFactor': {
        'type': CFloatType('c_float'),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
