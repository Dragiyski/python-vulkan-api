from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkOpaqueCaptureDescriptorDataCreateInfoEXT'
_member_list_ = ['sType', 'pNext', 'opaqueCaptureDescriptorData']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_OPAQUE_CAPTURE_DESCRIPTOR_DATA_CREATE_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'opaqueCaptureDescriptorData': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
}
_extends_ = {
    'VkAccelerationStructureCreateInfoKHR',
    'VkAccelerationStructureCreateInfoNV',
    'VkBufferCreateInfo',
    'VkImageCreateInfo',
    'VkImageViewCreateInfo',
    'VkSamplerCreateInfo',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
