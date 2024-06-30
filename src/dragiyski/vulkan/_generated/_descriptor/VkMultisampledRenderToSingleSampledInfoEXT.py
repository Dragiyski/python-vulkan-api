from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkMultisampledRenderToSingleSampledInfoEXT'
_member_list_ = ['sType', 'pNext', 'multisampledRenderToSingleSampledEnable', 'rasterizationSamples']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_MULTISAMPLED_RENDER_TO_SINGLE_SAMPLED_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'multisampledRenderToSingleSampledEnable': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'rasterizationSamples': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkSampleCountFlagBits',
        'is_string': False,
    },
}
_extends_ = {
    'VkRenderingInfo',
    'VkSubpassDescription2',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
