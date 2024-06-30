from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkWriteDescriptorSet'
_member_list_ = ['sType', 'pNext', 'dstSet', 'dstBinding', 'dstArrayElement', 'descriptorCount', 'descriptorType', 'pImageInfo', 'pBufferInfo', 'pTexelBufferView']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_WRITE_DESCRIPTOR_SET',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
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
    'descriptorType': {
        'type': CIntType('c_int'),
        'type_name': 'VkDescriptorType',
        'enum': 'VkDescriptorType',
        'is_string': False,
    },
    'pImageInfo': {
        'type': CPointerType(CComplexType('VkDescriptorImageInfo')),
        'type_name': 'VkDescriptorImageInfo',
        'structure': 'VkDescriptorImageInfo',
        'length': [['descriptorCount']],
        'is_string': False,
    },
    'pBufferInfo': {
        'type': CPointerType(CComplexType('VkDescriptorBufferInfo')),
        'type_name': 'VkDescriptorBufferInfo',
        'structure': 'VkDescriptorBufferInfo',
        'length': [['descriptorCount']],
        'is_string': False,
    },
    'pTexelBufferView': {
        'type': CPointerType(CIntType('c_void_p')),
        'length': [['descriptorCount']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkWriteDescriptorSetAccelerationStructureKHR',
    'VkWriteDescriptorSetAccelerationStructureNV',
    'VkWriteDescriptorSetInlineUniformBlock',
}
_includes_ = {
    'VkDescriptorBufferInfo',
    'VkDescriptorImageInfo',
}
_included_in_ = {
    'VkPushDescriptorSetInfoKHR',
}
_input_of_ = {
    'vkCmdPushDescriptorSetKHR',
    'vkUpdateDescriptorSets',
}
_output_of_ = set()
