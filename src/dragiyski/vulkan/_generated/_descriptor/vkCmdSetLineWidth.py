from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdSetLineWidth'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'lineWidth']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'lineWidth': {
        'type': CFloatType('c_float'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
