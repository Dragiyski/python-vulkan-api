import ctypes

class CType(ctypes.Structure):
    pass

from .VkDescriptorBufferInfo import CType as VkDescriptorBufferInfo
from .VkDescriptorImageInfo import CType as VkDescriptorImageInfo

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('dstSet', ctypes.c_void_p),
    ('dstBinding', ctypes.c_uint32),
    ('dstArrayElement', ctypes.c_uint32),
    ('descriptorCount', ctypes.c_uint32),
    ('descriptorType', ctypes.c_int),
    ('pImageInfo', ctypes.POINTER(VkDescriptorImageInfo)),
    ('pBufferInfo', ctypes.POINTER(VkDescriptorBufferInfo)),
    ('pTexelBufferView', ctypes.POINTER(ctypes.c_void_p)),
]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkWriteDescriptorSetAccelerationStructureKHR',
        'VkWriteDescriptorSetAccelerationStructureNV',
        'VkWriteDescriptorSetInlineUniformBlock',
    },
    'includes': {
        'VkDescriptorBufferInfo',
        'VkDescriptorImageInfo',
    },
    'included_in': {
        'VkPushDescriptorSetInfoKHR',
    },
    'input_of': {
        'vkCmdPushDescriptorSetKHR',
        'vkUpdateDescriptorSets',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_WRITE_DESCRIPTOR_SET', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'dstSet': {'python_name': ['dst', 'set']},
        'dstBinding': {'python_name': ['dst', 'binding']},
        'dstArrayElement': {'python_name': ['dst', 'array', 'element']},
        'descriptorCount': {'python_name': ['descriptor', 'count']},
        'descriptorType': {'python_name': ['descriptor', 'type'], 'type': 'VkDescriptorType'},
        'pImageInfo': {'python_name': ['p', 'image', 'info'], 'len': [['descriptorCount']], 'type': 'VkDescriptorImageInfo'},
        'pBufferInfo': {'python_name': ['p', 'buffer', 'info'], 'len': [['descriptorCount']], 'type': 'VkDescriptorBufferInfo'},
        'pTexelBufferView': {'python_name': ['p', 'texel', 'buffer', 'view'], 'len': [['descriptorCount']]},
    }
}
