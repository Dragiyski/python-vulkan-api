from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDevicePortabilitySubsetFeaturesKHR'
_member_list_ = ['sType', 'pNext', 'constantAlphaColorBlendFactors', 'events', 'imageViewFormatReinterpretation', 'imageViewFormatSwizzle', 'imageView2DOn3DImage', 'multisampleArrayImage', 'mutableComparisonSamplers', 'pointPolygons', 'samplerMipLodBias', 'separateStencilMaskRef', 'shaderSampleRateInterpolationFunctions', 'tessellationIsolines', 'tessellationPointMode', 'triangleFans', 'vertexAttributeAccessBeyondStride']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PORTABILITY_SUBSET_FEATURES_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'constantAlphaColorBlendFactors': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'events': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'imageViewFormatReinterpretation': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'imageViewFormatSwizzle': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'imageView2DOn3DImage': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'multisampleArrayImage': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'mutableComparisonSamplers': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pointPolygons': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'samplerMipLodBias': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'separateStencilMaskRef': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'shaderSampleRateInterpolationFunctions': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'tessellationIsolines': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'tessellationPointMode': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'triangleFans': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'vertexAttributeAccessBeyondStride': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = {
    'VkDeviceCreateInfo',
    'VkPhysicalDeviceFeatures2',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
