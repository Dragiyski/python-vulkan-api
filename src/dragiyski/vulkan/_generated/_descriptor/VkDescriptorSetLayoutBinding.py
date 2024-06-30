from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDescriptorSetLayoutBinding'
_member_list_ = ['binding', 'descriptorType', 'descriptorCount', 'stageFlags', 'pImmutableSamplers']
_member_info_ = {
    'binding': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'descriptorType': {
        'type': CIntType('c_int'),
        'type_name': 'VkDescriptorType',
        'enum': 'VkDescriptorType',
        'is_string': False,
    },
    'descriptorCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'stageFlags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkShaderStageFlags',
        'enum': 'VkShaderStageFlags',
        'is_string': False,
    },
    'pImmutableSamplers': {
        'type': CPointerType(CIntType('c_void_p')),
        'length': [['descriptorCount']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkDescriptorSetLayoutCreateInfo',
}
_input_of_ = set()
_output_of_ = set()
