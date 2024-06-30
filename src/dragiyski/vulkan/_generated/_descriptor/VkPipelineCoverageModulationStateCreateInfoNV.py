from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPipelineCoverageModulationStateCreateInfoNV'
_member_list_ = ['sType', 'pNext', 'flags', 'coverageModulationMode', 'coverageModulationTableEnable', 'coverageModulationTableCount', 'pCoverageModulationTable']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PIPELINE_COVERAGE_MODULATION_STATE_CREATE_INFO_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkPipelineCoverageModulationStateCreateFlagsNV',
        'enum': 'VkPipelineCoverageModulationStateCreateFlagsNV',
        'is_string': False,
    },
    'coverageModulationMode': {
        'type': CIntType('c_int'),
        'type_name': 'VkCoverageModulationModeNV',
        'enum': 'VkCoverageModulationModeNV',
        'is_string': False,
    },
    'coverageModulationTableEnable': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'coverageModulationTableCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pCoverageModulationTable': {
        'type': CPointerType(CFloatType('c_float')),
        'length': [['coverageModulationTableCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkPipelineMultisampleStateCreateInfo',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
