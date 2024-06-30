from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkMicromapBuildInfoEXT'
_member_list_ = ['sType', 'pNext', 'type', 'flags', 'mode', 'dstMicromap', 'usageCountsCount', 'pUsageCounts', 'ppUsageCounts', 'data', 'scratchData', 'triangleArray', 'triangleArrayStride']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_MICROMAP_BUILD_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'type': {
        'type': CIntType('c_int'),
        'type_name': 'VkMicromapTypeEXT',
        'enum': 'VkMicromapTypeEXT',
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkBuildMicromapFlagsEXT',
        'enum': 'VkBuildMicromapFlagsEXT',
        'is_string': False,
    },
    'mode': {
        'type': CIntType('c_int'),
        'type_name': 'VkBuildMicromapModeEXT',
        'enum': 'VkBuildMicromapModeEXT',
        'is_string': False,
    },
    'dstMicromap': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'usageCountsCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pUsageCounts': {
        'type': CPointerType(CComplexType('VkMicromapUsageEXT')),
        'type_name': 'VkMicromapUsageEXT',
        'structure': 'VkMicromapUsageEXT',
        'length': [['usageCountsCount']],
        'is_string': False,
    },
    'ppUsageCounts': {
        'type': CPointerType(CPointerType(CComplexType('VkMicromapUsageEXT'))),
        'type_name': 'VkMicromapUsageEXT',
        'structure': 'VkMicromapUsageEXT',
        'length': [['usageCountsCount'], 1],
        'is_string': False,
    },
    'data': {
        'type': CComplexType('VkDeviceOrHostAddressConstKHR'),
        'type_name': 'VkDeviceOrHostAddressConstKHR',
        'union': 'VkDeviceOrHostAddressConstKHR',
        'is_string': False,
    },
    'scratchData': {
        'type': CComplexType('VkDeviceOrHostAddressKHR'),
        'type_name': 'VkDeviceOrHostAddressKHR',
        'union': 'VkDeviceOrHostAddressKHR',
        'is_string': False,
    },
    'triangleArray': {
        'type': CComplexType('VkDeviceOrHostAddressConstKHR'),
        'type_name': 'VkDeviceOrHostAddressConstKHR',
        'union': 'VkDeviceOrHostAddressConstKHR',
        'is_string': False,
    },
    'triangleArrayStride': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkDeviceOrHostAddressConstKHR',
    'VkDeviceOrHostAddressKHR',
    'VkMicromapUsageEXT',
}
_included_in_ = set()
_input_of_ = {
    'vkBuildMicromapsEXT',
    'vkCmdBuildMicromapsEXT',
    'vkGetMicromapBuildSizesEXT',
}
_output_of_ = set()
