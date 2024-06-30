from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPipelineMultisampleStateCreateInfo'
_member_list_ = ['sType', 'pNext', 'flags', 'rasterizationSamples', 'sampleShadingEnable', 'minSampleShading', 'pSampleMask', 'alphaToCoverageEnable', 'alphaToOneEnable']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PIPELINE_MULTISAMPLE_STATE_CREATE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkPipelineMultisampleStateCreateFlags',
        'enum': 'VkPipelineMultisampleStateCreateFlags',
        'is_string': False,
    },
    'rasterizationSamples': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkSampleCountFlagBits',
        'is_string': False,
    },
    'sampleShadingEnable': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'minSampleShading': {
        'type': CFloatType('c_float'),
        'is_string': False,
    },
    'pSampleMask': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
    },
    'alphaToCoverageEnable': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'alphaToOneEnable': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkPipelineCoverageModulationStateCreateInfoNV',
    'VkPipelineCoverageReductionStateCreateInfoNV',
    'VkPipelineCoverageToColorStateCreateInfoNV',
    'VkPipelineSampleLocationsStateCreateInfoEXT',
}
_includes_ = set()
_included_in_ = {
    'VkGraphicsPipelineCreateInfo',
}
_input_of_ = set()
_output_of_ = set()
