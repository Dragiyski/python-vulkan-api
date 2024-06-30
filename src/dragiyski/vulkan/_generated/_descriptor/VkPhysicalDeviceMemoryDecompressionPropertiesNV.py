from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceMemoryDecompressionPropertiesNV'
_member_list_ = ['sType', 'pNext', 'decompressionMethods', 'maxDecompressionIndirectCount']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MEMORY_DECOMPRESSION_PROPERTIES_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'decompressionMethods': {
        'type': CIntType('c_uint64'),
        'type_name': 'VkMemoryDecompressionMethodFlagsNV',
        'enum': 'VkMemoryDecompressionMethodFlagsNV',
        'is_string': False,
    },
    'maxDecompressionIndirectCount': {
        'type': CIntType('c_uint64'),
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
