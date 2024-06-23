import ctypes

class CType(ctypes.Structure):
    pass

from .VkDescriptorPoolSize import CType as VkDescriptorPoolSize

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('maxSets', ctypes.c_uint32),
    ('poolSizeCount', ctypes.c_uint32),
    ('pPoolSizes', ctypes.POINTER(VkDescriptorPoolSize)),
]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkDescriptorPoolInlineUniformBlockCreateInfo',
        'VkMutableDescriptorTypeCreateInfoEXT',
    },
    'includes': {
        'VkDescriptorPoolSize',
    },
    'included_in': set(),
    'input_of': {
        'vkCreateDescriptorPool',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DESCRIPTOR_POOL_CREATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkDescriptorPoolCreateFlags'},
        'maxSets': {'python_name': ['max', 'sets']},
        'poolSizeCount': {'python_name': ['pool', 'size', 'count']},
        'pPoolSizes': {'python_name': ['p', 'pool', 'sizes'], 'len': [['poolSizeCount']], 'type': 'VkDescriptorPoolSize'},
    }
}
