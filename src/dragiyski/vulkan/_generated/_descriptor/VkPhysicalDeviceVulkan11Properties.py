from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceVulkan11Properties'
_member_list_ = ['sType', 'pNext', 'deviceUUID', 'driverUUID', 'deviceLUID', 'deviceNodeMask', 'deviceLUIDValid', 'subgroupSize', 'subgroupSupportedStages', 'subgroupSupportedOperations', 'subgroupQuadOperationsInAllStages', 'pointClippingBehavior', 'maxMultiviewViewCount', 'maxMultiviewInstanceIndex', 'protectedNoFault', 'maxPerSetDescriptors', 'maxMemoryAllocationSize']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VULKAN_1_1_PROPERTIES',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'deviceUUID': {
        'type': CArrayType(CIntType('c_uint8'), 16),
        'is_string': False,
    },
    'driverUUID': {
        'type': CArrayType(CIntType('c_uint8'), 16),
        'is_string': False,
    },
    'deviceLUID': {
        'type': CArrayType(CIntType('c_uint8'), 8),
        'is_string': False,
    },
    'deviceNodeMask': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'deviceLUIDValid': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'subgroupSize': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'subgroupSupportedStages': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkShaderStageFlags',
        'enum': 'VkShaderStageFlags',
        'is_string': False,
    },
    'subgroupSupportedOperations': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkSubgroupFeatureFlags',
        'enum': 'VkSubgroupFeatureFlags',
        'is_string': False,
    },
    'subgroupQuadOperationsInAllStages': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pointClippingBehavior': {
        'type': CIntType('c_int'),
        'type_name': 'VkPointClippingBehavior',
        'enum': 'VkPointClippingBehavior',
        'is_string': False,
    },
    'maxMultiviewViewCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxMultiviewInstanceIndex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'protectedNoFault': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxPerSetDescriptors': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxMemoryAllocationSize': {
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
