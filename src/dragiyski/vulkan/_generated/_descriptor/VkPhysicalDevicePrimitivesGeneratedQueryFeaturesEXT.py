from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDevicePrimitivesGeneratedQueryFeaturesEXT'
_member_list_ = ['sType', 'pNext', 'primitivesGeneratedQuery', 'primitivesGeneratedQueryWithRasterizerDiscard', 'primitivesGeneratedQueryWithNonZeroStreams']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PRIMITIVES_GENERATED_QUERY_FEATURES_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'primitivesGeneratedQuery': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'primitivesGeneratedQueryWithRasterizerDiscard': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'primitivesGeneratedQueryWithNonZeroStreams': {
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
