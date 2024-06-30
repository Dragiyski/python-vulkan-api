from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkAccelerationStructureCreateInfoKHR'
_member_list_ = ['sType', 'pNext', 'createFlags', 'buffer', 'offset', 'size', 'type', 'deviceAddress']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_CREATE_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'createFlags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkAccelerationStructureCreateFlagsKHR',
        'enum': 'VkAccelerationStructureCreateFlagsKHR',
        'is_string': False,
    },
    'buffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'offset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'size': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'type': {
        'type': CIntType('c_int'),
        'type_name': 'VkAccelerationStructureTypeKHR',
        'enum': 'VkAccelerationStructureTypeKHR',
        'is_string': False,
    },
    'deviceAddress': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkAccelerationStructureMotionInfoNV',
    'VkOpaqueCaptureDescriptorDataCreateInfoEXT',
}
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkCreateAccelerationStructureKHR',
}
_output_of_ = set()
