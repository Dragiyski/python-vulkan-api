from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkAccelerationStructureGeometryTrianglesDataKHR'
_member_list_ = ['sType', 'pNext', 'vertexFormat', 'vertexData', 'vertexStride', 'maxVertex', 'indexType', 'indexData', 'transformData']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_GEOMETRY_TRIANGLES_DATA_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'vertexFormat': {
        'type': CIntType('c_int'),
        'type_name': 'VkFormat',
        'enum': 'VkFormat',
        'is_string': False,
    },
    'vertexData': {
        'type': CComplexType('VkDeviceOrHostAddressConstKHR'),
        'type_name': 'VkDeviceOrHostAddressConstKHR',
        'union': 'VkDeviceOrHostAddressConstKHR',
        'is_string': False,
    },
    'vertexStride': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'maxVertex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'indexType': {
        'type': CIntType('c_int'),
        'type_name': 'VkIndexType',
        'enum': 'VkIndexType',
        'is_string': False,
    },
    'indexData': {
        'type': CComplexType('VkDeviceOrHostAddressConstKHR'),
        'type_name': 'VkDeviceOrHostAddressConstKHR',
        'union': 'VkDeviceOrHostAddressConstKHR',
        'is_string': False,
    },
    'transformData': {
        'type': CComplexType('VkDeviceOrHostAddressConstKHR'),
        'type_name': 'VkDeviceOrHostAddressConstKHR',
        'union': 'VkDeviceOrHostAddressConstKHR',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkAccelerationStructureGeometryMotionTrianglesDataNV',
    'VkAccelerationStructureTrianglesDisplacementMicromapNV',
    'VkAccelerationStructureTrianglesOpacityMicromapEXT',
}
_includes_ = {
    'VkDeviceOrHostAddressConstKHR',
}
_included_in_ = {
    'VkAccelerationStructureGeometryDataKHR',
}
_input_of_ = set()
_output_of_ = set()
