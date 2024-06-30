from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkAccelerationStructureMotionInstanceNV'
_member_list_ = ['type', 'flags', 'data']
_member_info_ = {
    'type': {
        'type': CIntType('c_int'),
        'type_name': 'VkAccelerationStructureMotionInstanceTypeNV',
        'enum': 'VkAccelerationStructureMotionInstanceTypeNV',
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkAccelerationStructureMotionInstanceFlagsNV',
        'enum': 'VkAccelerationStructureMotionInstanceFlagsNV',
        'is_string': False,
    },
    'data': {
        'type': CComplexType('VkAccelerationStructureMotionInstanceDataNV'),
        'type_name': 'VkAccelerationStructureMotionInstanceDataNV',
        'union': 'VkAccelerationStructureMotionInstanceDataNV',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkAccelerationStructureMotionInstanceDataNV',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
