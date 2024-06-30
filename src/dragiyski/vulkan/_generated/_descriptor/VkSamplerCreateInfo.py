from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSamplerCreateInfo'
_member_list_ = ['sType', 'pNext', 'flags', 'magFilter', 'minFilter', 'mipmapMode', 'addressModeU', 'addressModeV', 'addressModeW', 'mipLodBias', 'anisotropyEnable', 'maxAnisotropy', 'compareEnable', 'compareOp', 'minLod', 'maxLod', 'borderColor', 'unnormalizedCoordinates']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_SAMPLER_CREATE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkSamplerCreateFlags',
        'enum': 'VkSamplerCreateFlags',
        'is_string': False,
    },
    'magFilter': {
        'type': CIntType('c_int'),
        'type_name': 'VkFilter',
        'enum': 'VkFilter',
        'is_string': False,
    },
    'minFilter': {
        'type': CIntType('c_int'),
        'type_name': 'VkFilter',
        'enum': 'VkFilter',
        'is_string': False,
    },
    'mipmapMode': {
        'type': CIntType('c_int'),
        'type_name': 'VkSamplerMipmapMode',
        'enum': 'VkSamplerMipmapMode',
        'is_string': False,
    },
    'addressModeU': {
        'type': CIntType('c_int'),
        'type_name': 'VkSamplerAddressMode',
        'enum': 'VkSamplerAddressMode',
        'is_string': False,
    },
    'addressModeV': {
        'type': CIntType('c_int'),
        'type_name': 'VkSamplerAddressMode',
        'enum': 'VkSamplerAddressMode',
        'is_string': False,
    },
    'addressModeW': {
        'type': CIntType('c_int'),
        'type_name': 'VkSamplerAddressMode',
        'enum': 'VkSamplerAddressMode',
        'is_string': False,
    },
    'mipLodBias': {
        'type': CFloatType('c_float'),
        'is_string': False,
    },
    'anisotropyEnable': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxAnisotropy': {
        'type': CFloatType('c_float'),
        'is_string': False,
    },
    'compareEnable': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'compareOp': {
        'type': CIntType('c_int'),
        'type_name': 'VkCompareOp',
        'enum': 'VkCompareOp',
        'is_string': False,
    },
    'minLod': {
        'type': CFloatType('c_float'),
        'is_string': False,
    },
    'maxLod': {
        'type': CFloatType('c_float'),
        'is_string': False,
    },
    'borderColor': {
        'type': CIntType('c_int'),
        'type_name': 'VkBorderColor',
        'enum': 'VkBorderColor',
        'is_string': False,
    },
    'unnormalizedCoordinates': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkOpaqueCaptureDescriptorDataCreateInfoEXT',
    'VkSamplerBlockMatchWindowCreateInfoQCOM',
    'VkSamplerBorderColorComponentMappingCreateInfoEXT',
    'VkSamplerCubicWeightsCreateInfoQCOM',
    'VkSamplerCustomBorderColorCreateInfoEXT',
    'VkSamplerReductionModeCreateInfo',
    'VkSamplerYcbcrConversionInfo',
}
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkCreateSampler',
}
_output_of_ = set()
