from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdSetLineRasterizationModeEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'lineRasterizationMode']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'lineRasterizationMode': {
        'type': CIntType('c_int'),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
