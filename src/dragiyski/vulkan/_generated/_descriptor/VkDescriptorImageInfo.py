from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDescriptorImageInfo'
_member_list_ = ['sampler', 'imageView', 'imageLayout']
_member_info_ = {
    'sampler': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'imageView': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'imageLayout': {
        'type': CIntType('c_int'),
        'type_name': 'VkImageLayout',
        'enum': 'VkImageLayout',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkDescriptorDataEXT',
    'VkWriteDescriptorSet',
}
_input_of_ = set()
_output_of_ = set()
