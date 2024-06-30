from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceFragmentShadingRatePropertiesKHR'
_member_list_ = ['sType', 'pNext', 'minFragmentShadingRateAttachmentTexelSize', 'maxFragmentShadingRateAttachmentTexelSize', 'maxFragmentShadingRateAttachmentTexelSizeAspectRatio', 'primitiveFragmentShadingRateWithMultipleViewports', 'layeredShadingRateAttachments', 'fragmentShadingRateNonTrivialCombinerOps', 'maxFragmentSize', 'maxFragmentSizeAspectRatio', 'maxFragmentShadingRateCoverageSamples', 'maxFragmentShadingRateRasterizationSamples', 'fragmentShadingRateWithShaderDepthStencilWrites', 'fragmentShadingRateWithSampleMask', 'fragmentShadingRateWithShaderSampleMask', 'fragmentShadingRateWithConservativeRasterization', 'fragmentShadingRateWithFragmentShaderInterlock', 'fragmentShadingRateWithCustomSampleLocations', 'fragmentShadingRateStrictMultiplyCombiner']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_SHADING_RATE_PROPERTIES_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'minFragmentShadingRateAttachmentTexelSize': {
        'type': CComplexType('VkExtent2D'),
        'type_name': 'VkExtent2D',
        'structure': 'VkExtent2D',
        'is_string': False,
    },
    'maxFragmentShadingRateAttachmentTexelSize': {
        'type': CComplexType('VkExtent2D'),
        'type_name': 'VkExtent2D',
        'structure': 'VkExtent2D',
        'is_string': False,
    },
    'maxFragmentShadingRateAttachmentTexelSizeAspectRatio': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'primitiveFragmentShadingRateWithMultipleViewports': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'layeredShadingRateAttachments': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'fragmentShadingRateNonTrivialCombinerOps': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxFragmentSize': {
        'type': CComplexType('VkExtent2D'),
        'type_name': 'VkExtent2D',
        'structure': 'VkExtent2D',
        'is_string': False,
    },
    'maxFragmentSizeAspectRatio': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxFragmentShadingRateCoverageSamples': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxFragmentShadingRateRasterizationSamples': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkSampleCountFlagBits',
        'is_string': False,
    },
    'fragmentShadingRateWithShaderDepthStencilWrites': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'fragmentShadingRateWithSampleMask': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'fragmentShadingRateWithShaderSampleMask': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'fragmentShadingRateWithConservativeRasterization': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'fragmentShadingRateWithFragmentShaderInterlock': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'fragmentShadingRateWithCustomSampleLocations': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'fragmentShadingRateStrictMultiplyCombiner': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = {
    'VkPhysicalDeviceProperties2',
}
_extended_by_ = set()
_includes_ = {
    'VkExtent2D',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
