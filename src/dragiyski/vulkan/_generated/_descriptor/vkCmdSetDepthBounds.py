from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdSetDepthBounds'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'minDepthBounds', 'maxDepthBounds']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'minDepthBounds': {
        'type': CFloatType('c_float'),
        'is_string': False,
        'output': False,
    },
    'maxDepthBounds': {
        'type': CFloatType('c_float'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
