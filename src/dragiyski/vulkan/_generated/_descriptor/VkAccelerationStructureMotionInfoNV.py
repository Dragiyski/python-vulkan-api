from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkAccelerationStructureMotionInfoNV'
_member_list_ = ['sType', 'pNext', 'maxInstances', 'flags']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_MOTION_INFO_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'maxInstances': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkAccelerationStructureMotionInfoFlagsNV',
        'enum': 'VkAccelerationStructureMotionInfoFlagsNV',
        'is_string': False,
    },
}
_extends_ = {
    'VkAccelerationStructureCreateInfoKHR',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
