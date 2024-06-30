from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkAccelerationStructureTrianglesDisplacementMicromapNV'
_member_list_ = ['sType', 'pNext', 'displacementBiasAndScaleFormat', 'displacementVectorFormat', 'displacementBiasAndScaleBuffer', 'displacementBiasAndScaleStride', 'displacementVectorBuffer', 'displacementVectorStride', 'displacedMicromapPrimitiveFlags', 'displacedMicromapPrimitiveFlagsStride', 'indexType', 'indexBuffer', 'indexStride', 'baseTriangle', 'usageCountsCount', 'pUsageCounts', 'ppUsageCounts', 'micromap']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_TRIANGLES_DISPLACEMENT_MICROMAP_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'displacementBiasAndScaleFormat': {
        'type': CIntType('c_int'),
        'type_name': 'VkFormat',
        'enum': 'VkFormat',
        'is_string': False,
    },
    'displacementVectorFormat': {
        'type': CIntType('c_int'),
        'type_name': 'VkFormat',
        'enum': 'VkFormat',
        'is_string': False,
    },
    'displacementBiasAndScaleBuffer': {
        'type': CComplexType('VkDeviceOrHostAddressConstKHR'),
        'type_name': 'VkDeviceOrHostAddressConstKHR',
        'union': 'VkDeviceOrHostAddressConstKHR',
        'is_string': False,
    },
    'displacementBiasAndScaleStride': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'displacementVectorBuffer': {
        'type': CComplexType('VkDeviceOrHostAddressConstKHR'),
        'type_name': 'VkDeviceOrHostAddressConstKHR',
        'union': 'VkDeviceOrHostAddressConstKHR',
        'is_string': False,
    },
    'displacementVectorStride': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'displacedMicromapPrimitiveFlags': {
        'type': CComplexType('VkDeviceOrHostAddressConstKHR'),
        'type_name': 'VkDeviceOrHostAddressConstKHR',
        'union': 'VkDeviceOrHostAddressConstKHR',
        'is_string': False,
    },
    'displacedMicromapPrimitiveFlagsStride': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'indexType': {
        'type': CIntType('c_int'),
        'type_name': 'VkIndexType',
        'enum': 'VkIndexType',
        'is_string': False,
    },
    'indexBuffer': {
        'type': CComplexType('VkDeviceOrHostAddressConstKHR'),
        'type_name': 'VkDeviceOrHostAddressConstKHR',
        'union': 'VkDeviceOrHostAddressConstKHR',
        'is_string': False,
    },
    'indexStride': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'baseTriangle': {
        'type': CIntType('c_uint32'),
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
    'micromap': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
}
_extends_ = {
    'VkAccelerationStructureGeometryTrianglesDataKHR',
}
_extended_by_ = set()
_includes_ = {
    'VkDeviceOrHostAddressConstKHR',
    'VkMicromapUsageEXT',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
