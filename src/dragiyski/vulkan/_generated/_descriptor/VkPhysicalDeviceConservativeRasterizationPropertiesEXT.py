from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceConservativeRasterizationPropertiesEXT'
_member_list_ = ['sType', 'pNext', 'primitiveOverestimationSize', 'maxExtraPrimitiveOverestimationSize', 'extraPrimitiveOverestimationSizeGranularity', 'primitiveUnderestimation', 'conservativePointAndLineRasterization', 'degenerateTrianglesRasterized', 'degenerateLinesRasterized', 'fullyCoveredFragmentShaderInputVariable', 'conservativeRasterizationPostDepthCoverage']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_CONSERVATIVE_RASTERIZATION_PROPERTIES_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'primitiveOverestimationSize': {
        'type': CFloatType('c_float'),
        'is_string': False,
    },
    'maxExtraPrimitiveOverestimationSize': {
        'type': CFloatType('c_float'),
        'is_string': False,
    },
    'extraPrimitiveOverestimationSizeGranularity': {
        'type': CFloatType('c_float'),
        'is_string': False,
    },
    'primitiveUnderestimation': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'conservativePointAndLineRasterization': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'degenerateTrianglesRasterized': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'degenerateLinesRasterized': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'fullyCoveredFragmentShaderInputVariable': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'conservativeRasterizationPostDepthCoverage': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = {
    'VkPhysicalDeviceProperties2',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
