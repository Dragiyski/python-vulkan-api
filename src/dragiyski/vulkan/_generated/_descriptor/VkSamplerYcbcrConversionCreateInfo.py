from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSamplerYcbcrConversionCreateInfo'
_member_list_ = ['sType', 'pNext', 'format', 'ycbcrModel', 'ycbcrRange', 'components', 'xChromaOffset', 'yChromaOffset', 'chromaFilter', 'forceExplicitReconstruction']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_SAMPLER_YCBCR_CONVERSION_CREATE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'format': {
        'type': CIntType('c_int'),
        'type_name': 'VkFormat',
        'enum': 'VkFormat',
        'is_string': False,
    },
    'ycbcrModel': {
        'type': CIntType('c_int'),
        'type_name': 'VkSamplerYcbcrModelConversion',
        'enum': 'VkSamplerYcbcrModelConversion',
        'is_string': False,
    },
    'ycbcrRange': {
        'type': CIntType('c_int'),
        'type_name': 'VkSamplerYcbcrRange',
        'enum': 'VkSamplerYcbcrRange',
        'is_string': False,
    },
    'components': {
        'type': CComplexType('VkComponentMapping'),
        'type_name': 'VkComponentMapping',
        'structure': 'VkComponentMapping',
        'is_string': False,
    },
    'xChromaOffset': {
        'type': CIntType('c_int'),
        'type_name': 'VkChromaLocation',
        'enum': 'VkChromaLocation',
        'is_string': False,
    },
    'yChromaOffset': {
        'type': CIntType('c_int'),
        'type_name': 'VkChromaLocation',
        'enum': 'VkChromaLocation',
        'is_string': False,
    },
    'chromaFilter': {
        'type': CIntType('c_int'),
        'type_name': 'VkFilter',
        'enum': 'VkFilter',
        'is_string': False,
    },
    'forceExplicitReconstruction': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkExternalFormatANDROID',
    'VkExternalFormatQNX',
    'VkSamplerYcbcrConversionYcbcrDegammaCreateInfoQCOM',
}
_includes_ = {
    'VkComponentMapping',
}
_included_in_ = set()
_input_of_ = {
    'vkCreateSamplerYcbcrConversion',
}
_output_of_ = set()
