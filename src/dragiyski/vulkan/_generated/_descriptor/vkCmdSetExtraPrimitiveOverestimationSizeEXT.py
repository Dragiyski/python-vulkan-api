from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdSetExtraPrimitiveOverestimationSizeEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'extraPrimitiveOverestimationSize']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'extraPrimitiveOverestimationSize': {
        'type': CFloatType('c_float'),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
