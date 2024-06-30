from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkAccelerationStructureInfoNV'
_member_list_ = ['sType', 'pNext', 'type', 'flags', 'instanceCount', 'geometryCount', 'pGeometries']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_INFO_NV',
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
    'instanceCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'geometryCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pGeometries': {
        'type': CPointerType(CComplexType('VkGeometryNV')),
        'type_name': 'VkGeometryNV',
        'structure': 'VkGeometryNV',
        'length': [['geometryCount']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkGeometryNV',
}
_included_in_ = {
    'VkAccelerationStructureCreateInfoNV',
}
_input_of_ = {
    'vkCmdBuildAccelerationStructureNV',
}
_output_of_ = set()
