from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdSetCoverageReductionModeNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'coverageReductionMode']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'coverageReductionMode': {
        'type': CIntType('c_int'),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
