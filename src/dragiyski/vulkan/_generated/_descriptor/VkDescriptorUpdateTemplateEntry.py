from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDescriptorUpdateTemplateEntry'
_member_list_ = ['dstBinding', 'dstArrayElement', 'descriptorCount', 'descriptorType', 'offset', 'stride']
_member_info_ = {
    'dstBinding': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'dstArrayElement': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'descriptorCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'descriptorType': {
        'type': CIntType('c_int'),
        'type_name': 'VkDescriptorType',
        'enum': 'VkDescriptorType',
        'is_string': False,
    },
    'offset': {
        'type': CIntType('c_size_t'),
        'is_string': False,
    },
    'stride': {
        'type': CIntType('c_size_t'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkDescriptorUpdateTemplateCreateInfo',
}
_input_of_ = set()
_output_of_ = set()
