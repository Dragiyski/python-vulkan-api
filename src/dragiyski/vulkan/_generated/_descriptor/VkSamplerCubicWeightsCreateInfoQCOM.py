from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSamplerCubicWeightsCreateInfoQCOM'
_member_list_ = ['sType', 'pNext', 'cubicWeights']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_SAMPLER_CUBIC_WEIGHTS_CREATE_INFO_QCOM',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'cubicWeights': {
        'type': CIntType('c_int'),
        'type_name': 'VkCubicFilterWeightsQCOM',
        'enum': 'VkCubicFilterWeightsQCOM',
        'is_string': False,
    },
}
_extends_ = {
    'VkSamplerCreateInfo',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
