from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkAccelerationStructureGeometryInstancesDataKHR'
_member_list_ = ['sType', 'pNext', 'arrayOfPointers', 'data']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_GEOMETRY_INSTANCES_DATA_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'arrayOfPointers': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'data': {
        'type': CComplexType('VkDeviceOrHostAddressConstKHR'),
        'type_name': 'VkDeviceOrHostAddressConstKHR',
        'union': 'VkDeviceOrHostAddressConstKHR',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkDeviceOrHostAddressConstKHR',
}
_included_in_ = {
    'VkAccelerationStructureGeometryDataKHR',
}
_input_of_ = set()
_output_of_ = set()
