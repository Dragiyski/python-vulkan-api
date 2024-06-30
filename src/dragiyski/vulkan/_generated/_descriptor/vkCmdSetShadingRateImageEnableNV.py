from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdSetShadingRateImageEnableNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'shadingRateImageEnable']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'shadingRateImageEnable': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
