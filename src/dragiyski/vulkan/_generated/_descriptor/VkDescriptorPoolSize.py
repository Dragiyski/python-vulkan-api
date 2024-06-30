from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDescriptorPoolSize'
_member_list_ = ['type', 'descriptorCount']
_member_info_ = {
    'type': {
        'type': CIntType('c_int'),
        'type_name': 'VkDescriptorType',
        'enum': 'VkDescriptorType',
        'is_string': False,
    },
    'descriptorCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkDescriptorPoolCreateInfo',
}
_input_of_ = set()
_output_of_ = set()
