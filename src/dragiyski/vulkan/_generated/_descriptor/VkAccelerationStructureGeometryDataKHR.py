from ..._ctypes import *

_category_ = 'union'
_name_ = 'VkAccelerationStructureGeometryDataKHR'
_member_list_ = ['triangles', 'aabbs', 'instances']
_member_info_ = {
    'triangles': {
        'type': CComplexType('VkAccelerationStructureGeometryTrianglesDataKHR'),
        'type_name': 'VkAccelerationStructureGeometryTrianglesDataKHR',
        'structure': 'VkAccelerationStructureGeometryTrianglesDataKHR',
        'is_string': False,
    },
    'aabbs': {
        'type': CComplexType('VkAccelerationStructureGeometryAabbsDataKHR'),
        'type_name': 'VkAccelerationStructureGeometryAabbsDataKHR',
        'structure': 'VkAccelerationStructureGeometryAabbsDataKHR',
        'is_string': False,
    },
    'instances': {
        'type': CComplexType('VkAccelerationStructureGeometryInstancesDataKHR'),
        'type_name': 'VkAccelerationStructureGeometryInstancesDataKHR',
        'structure': 'VkAccelerationStructureGeometryInstancesDataKHR',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkAccelerationStructureGeometryAabbsDataKHR',
    'VkAccelerationStructureGeometryInstancesDataKHR',
    'VkAccelerationStructureGeometryTrianglesDataKHR',
}
_included_in_ = {
    'VkAccelerationStructureGeometryKHR',
}
_input_of_ = set()
_output_of_ = set()
