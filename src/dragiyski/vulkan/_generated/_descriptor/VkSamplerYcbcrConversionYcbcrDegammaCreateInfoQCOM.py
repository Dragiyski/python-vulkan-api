from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSamplerYcbcrConversionYcbcrDegammaCreateInfoQCOM'
_member_list_ = ['sType', 'pNext', 'enableYDegamma', 'enableCbCrDegamma']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_SAMPLER_YCBCR_CONVERSION_YCBCR_DEGAMMA_CREATE_INFO_QCOM',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'enableYDegamma': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'enableCbCrDegamma': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = {
    'VkSamplerYcbcrConversionCreateInfo',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
