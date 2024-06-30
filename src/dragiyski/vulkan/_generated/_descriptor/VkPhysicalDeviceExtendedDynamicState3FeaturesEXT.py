from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceExtendedDynamicState3FeaturesEXT'
_member_list_ = ['sType', 'pNext', 'extendedDynamicState3TessellationDomainOrigin', 'extendedDynamicState3DepthClampEnable', 'extendedDynamicState3PolygonMode', 'extendedDynamicState3RasterizationSamples', 'extendedDynamicState3SampleMask', 'extendedDynamicState3AlphaToCoverageEnable', 'extendedDynamicState3AlphaToOneEnable', 'extendedDynamicState3LogicOpEnable', 'extendedDynamicState3ColorBlendEnable', 'extendedDynamicState3ColorBlendEquation', 'extendedDynamicState3ColorWriteMask', 'extendedDynamicState3RasterizationStream', 'extendedDynamicState3ConservativeRasterizationMode', 'extendedDynamicState3ExtraPrimitiveOverestimationSize', 'extendedDynamicState3DepthClipEnable', 'extendedDynamicState3SampleLocationsEnable', 'extendedDynamicState3ColorBlendAdvanced', 'extendedDynamicState3ProvokingVertexMode', 'extendedDynamicState3LineRasterizationMode', 'extendedDynamicState3LineStippleEnable', 'extendedDynamicState3DepthClipNegativeOneToOne', 'extendedDynamicState3ViewportWScalingEnable', 'extendedDynamicState3ViewportSwizzle', 'extendedDynamicState3CoverageToColorEnable', 'extendedDynamicState3CoverageToColorLocation', 'extendedDynamicState3CoverageModulationMode', 'extendedDynamicState3CoverageModulationTableEnable', 'extendedDynamicState3CoverageModulationTable', 'extendedDynamicState3CoverageReductionMode', 'extendedDynamicState3RepresentativeFragmentTestEnable', 'extendedDynamicState3ShadingRateImageEnable']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTENDED_DYNAMIC_STATE_3_FEATURES_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'extendedDynamicState3TessellationDomainOrigin': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'extendedDynamicState3DepthClampEnable': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'extendedDynamicState3PolygonMode': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'extendedDynamicState3RasterizationSamples': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'extendedDynamicState3SampleMask': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'extendedDynamicState3AlphaToCoverageEnable': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'extendedDynamicState3AlphaToOneEnable': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'extendedDynamicState3LogicOpEnable': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'extendedDynamicState3ColorBlendEnable': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'extendedDynamicState3ColorBlendEquation': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'extendedDynamicState3ColorWriteMask': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'extendedDynamicState3RasterizationStream': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'extendedDynamicState3ConservativeRasterizationMode': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'extendedDynamicState3ExtraPrimitiveOverestimationSize': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'extendedDynamicState3DepthClipEnable': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'extendedDynamicState3SampleLocationsEnable': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'extendedDynamicState3ColorBlendAdvanced': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'extendedDynamicState3ProvokingVertexMode': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'extendedDynamicState3LineRasterizationMode': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'extendedDynamicState3LineStippleEnable': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'extendedDynamicState3DepthClipNegativeOneToOne': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'extendedDynamicState3ViewportWScalingEnable': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'extendedDynamicState3ViewportSwizzle': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'extendedDynamicState3CoverageToColorEnable': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'extendedDynamicState3CoverageToColorLocation': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'extendedDynamicState3CoverageModulationMode': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'extendedDynamicState3CoverageModulationTableEnable': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'extendedDynamicState3CoverageModulationTable': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'extendedDynamicState3CoverageReductionMode': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'extendedDynamicState3RepresentativeFragmentTestEnable': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'extendedDynamicState3ShadingRateImageEnable': {
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
