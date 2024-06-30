from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkFramebufferMixedSamplesCombinationNV'
_member_list_ = ['sType', 'pNext', 'coverageReductionMode', 'rasterizationSamples', 'depthStencilSamples', 'colorSamples']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_FRAMEBUFFER_MIXED_SAMPLES_COMBINATION_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'coverageReductionMode': {
        'type': CIntType('c_int'),
        'type_name': 'VkCoverageReductionModeNV',
        'enum': 'VkCoverageReductionModeNV',
        'is_string': False,
    },
    'rasterizationSamples': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkSampleCountFlagBits',
        'is_string': False,
    },
    'depthStencilSamples': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkSampleCountFlags',
        'enum': 'VkSampleCountFlags',
        'is_string': False,
    },
    'colorSamples': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkSampleCountFlags',
        'enum': 'VkSampleCountFlags',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = {
    'vkGetPhysicalDeviceSupportedFramebufferMixedSamplesCombinationsNV',
}
