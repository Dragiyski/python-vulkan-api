from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdSetFragmentShadingRateEnumNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'shadingRate', 'combinerOps']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'shadingRate': {
        'type': CIntType('c_int'),
        'is_string': False,
    },
    'combinerOps': {
        'type': CArrayType(CIntType('c_int'), 2),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
