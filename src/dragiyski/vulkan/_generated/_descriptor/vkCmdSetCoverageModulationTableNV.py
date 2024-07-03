from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdSetCoverageModulationTableNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'coverageModulationTableCount', 'pCoverageModulationTable']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'coverageModulationTableCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pCoverageModulationTable': {
        'type': CPointerType(CFloatType('c_float')),
        'is_string': False,
        'length': [['coverageModulationTableCount']],
        'output': False,
    },
}
_return_type_ = CVoidType()
