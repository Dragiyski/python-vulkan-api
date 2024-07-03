from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdSetExtraPrimitiveOverestimationSizeEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'extraPrimitiveOverestimationSize']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'extraPrimitiveOverestimationSize': {
        'type': CFloatType('c_float'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
