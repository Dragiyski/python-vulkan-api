from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkAccelerationStructureBuildGeometryInfoKHR'
_member_list_ = ['sType', 'pNext', 'type', 'flags', 'mode', 'srcAccelerationStructure', 'dstAccelerationStructure', 'geometryCount', 'pGeometries', 'ppGeometries', 'scratchData']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_BUILD_GEOMETRY_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'type': {
        'type': CIntType('c_int'),
        'type_name': 'VkAccelerationStructureTypeKHR',
        'enum': 'VkAccelerationStructureTypeKHR',
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkBuildAccelerationStructureFlagsKHR',
        'enum': 'VkBuildAccelerationStructureFlagsKHR',
        'is_string': False,
    },
    'mode': {
        'type': CIntType('c_int'),
        'type_name': 'VkBuildAccelerationStructureModeKHR',
        'enum': 'VkBuildAccelerationStructureModeKHR',
        'is_string': False,
    },
    'srcAccelerationStructure': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'dstAccelerationStructure': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'geometryCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pGeometries': {
        'type': CPointerType(CComplexType('VkAccelerationStructureGeometryKHR')),
        'type_name': 'VkAccelerationStructureGeometryKHR',
        'structure': 'VkAccelerationStructureGeometryKHR',
        'length': [['geometryCount']],
        'is_string': False,
    },
    'ppGeometries': {
        'type': CPointerType(CPointerType(CComplexType('VkAccelerationStructureGeometryKHR'))),
        'type_name': 'VkAccelerationStructureGeometryKHR',
        'structure': 'VkAccelerationStructureGeometryKHR',
        'length': [['geometryCount'], 1],
        'is_string': False,
    },
    'scratchData': {
        'type': CComplexType('VkDeviceOrHostAddressKHR'),
        'type_name': 'VkDeviceOrHostAddressKHR',
        'union': 'VkDeviceOrHostAddressKHR',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkAccelerationStructureGeometryKHR',
    'VkDeviceOrHostAddressKHR',
}
_included_in_ = set()
_input_of_ = {
    'vkBuildAccelerationStructuresKHR',
    'vkCmdBuildAccelerationStructuresIndirectKHR',
    'vkCmdBuildAccelerationStructuresKHR',
    'vkGetAccelerationStructureBuildSizesKHR',
}
_output_of_ = set()
