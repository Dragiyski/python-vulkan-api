from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceAccelerationStructurePropertiesKHR'
_member_list_ = ['sType', 'pNext', 'maxGeometryCount', 'maxInstanceCount', 'maxPrimitiveCount', 'maxPerStageDescriptorAccelerationStructures', 'maxPerStageDescriptorUpdateAfterBindAccelerationStructures', 'maxDescriptorSetAccelerationStructures', 'maxDescriptorSetUpdateAfterBindAccelerationStructures', 'minAccelerationStructureScratchOffsetAlignment']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_ACCELERATION_STRUCTURE_PROPERTIES_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'maxGeometryCount': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'maxInstanceCount': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'maxPrimitiveCount': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'maxPerStageDescriptorAccelerationStructures': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxPerStageDescriptorUpdateAfterBindAccelerationStructures': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxDescriptorSetAccelerationStructures': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxDescriptorSetUpdateAfterBindAccelerationStructures': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'minAccelerationStructureScratchOffsetAlignment': {
        'type': CIntType('c_uint32'),
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
