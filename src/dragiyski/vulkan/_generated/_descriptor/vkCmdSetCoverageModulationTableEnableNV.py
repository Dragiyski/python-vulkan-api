from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdSetCoverageModulationTableEnableNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'coverageModulationTableEnable']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'coverageModulationTableEnable': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
