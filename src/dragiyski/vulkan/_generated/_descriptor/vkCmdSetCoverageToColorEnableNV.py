from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdSetCoverageToColorEnableNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'coverageToColorEnable']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'coverageToColorEnable': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
