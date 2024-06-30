from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkAccelerationStructureCreateInfoNV'
_member_list_ = ['sType', 'pNext', 'compactedSize', 'info']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_CREATE_INFO_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'compactedSize': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'info': {
        'type': CComplexType('VkAccelerationStructureInfoNV'),
        'type_name': 'VkAccelerationStructureInfoNV',
        'structure': 'VkAccelerationStructureInfoNV',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkOpaqueCaptureDescriptorDataCreateInfoEXT',
}
_includes_ = {
    'VkAccelerationStructureInfoNV',
}
_included_in_ = set()
_input_of_ = {
    'vkCreateAccelerationStructureNV',
}
_output_of_ = set()
