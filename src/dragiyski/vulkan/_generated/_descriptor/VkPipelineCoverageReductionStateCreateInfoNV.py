from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPipelineCoverageReductionStateCreateInfoNV'
_member_list_ = ['sType', 'pNext', 'flags', 'coverageReductionMode']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PIPELINE_COVERAGE_REDUCTION_STATE_CREATE_INFO_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkPipelineCoverageReductionStateCreateFlagsNV',
        'enum': 'VkPipelineCoverageReductionStateCreateFlagsNV',
        'is_string': False,
    },
    'coverageReductionMode': {
        'type': CIntType('c_int'),
        'type_name': 'VkCoverageReductionModeNV',
        'enum': 'VkCoverageReductionModeNV',
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
