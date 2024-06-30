from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkImageViewHandleInfoNVX'
_member_list_ = ['sType', 'pNext', 'imageView', 'descriptorType', 'sampler']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_IMAGE_VIEW_HANDLE_INFO_NVX',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'imageView': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'descriptorType': {
        'type': CIntType('c_int'),
        'type_name': 'VkDescriptorType',
        'enum': 'VkDescriptorType',
        'is_string': False,
    },
    'sampler': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkGetImageViewHandleNVX',
}
_output_of_ = set()
