from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkCopyDescriptorSet'
_member_list_ = ['sType', 'pNext', 'srcSet', 'srcBinding', 'srcArrayElement', 'dstSet', 'dstBinding', 'dstArrayElement', 'descriptorCount']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_COPY_DESCRIPTOR_SET',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'srcSet': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'srcBinding': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'srcArrayElement': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'dstSet': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
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
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkUpdateDescriptorSets',
}
_output_of_ = set()
