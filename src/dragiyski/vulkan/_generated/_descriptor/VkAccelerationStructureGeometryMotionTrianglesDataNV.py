from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkAccelerationStructureGeometryMotionTrianglesDataNV'
_member_list_ = ['sType', 'pNext', 'vertexData']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_GEOMETRY_MOTION_TRIANGLES_DATA_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'vertexData': {
        'type': CComplexType('VkDeviceOrHostAddressConstKHR'),
        'type_name': 'VkDeviceOrHostAddressConstKHR',
        'union': 'VkDeviceOrHostAddressConstKHR',
        'is_string': False,
    },
}
_extends_ = {
    'VkAccelerationStructureGeometryTrianglesDataKHR',
}
_extended_by_ = set()
_includes_ = {
    'VkDeviceOrHostAddressConstKHR',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
