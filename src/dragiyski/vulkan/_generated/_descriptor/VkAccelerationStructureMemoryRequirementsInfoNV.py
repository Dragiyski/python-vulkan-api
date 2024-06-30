from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkAccelerationStructureMemoryRequirementsInfoNV'
_member_list_ = ['sType', 'pNext', 'type', 'accelerationStructure']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_MEMORY_REQUIREMENTS_INFO_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'type': {
        'type': CIntType('c_int'),
        'type_name': 'VkAccelerationStructureMemoryRequirementsTypeNV',
        'enum': 'VkAccelerationStructureMemoryRequirementsTypeNV',
        'is_string': False,
    },
    'accelerationStructure': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkGetAccelerationStructureMemoryRequirementsNV',
}
_output_of_ = set()
