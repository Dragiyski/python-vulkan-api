import ctypes

class CType(ctypes.Structure):
    pass

from .VkDescriptorSetLayoutBinding import CType as VkDescriptorSetLayoutBinding

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('bindingCount', ctypes.c_uint32),
    ('pBindings', ctypes.POINTER(VkDescriptorSetLayoutBinding)),
]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkDescriptorSetLayoutBindingFlagsCreateInfo',
        'VkMutableDescriptorTypeCreateInfoEXT',
    },
    'includes': {
        'VkDescriptorSetLayoutBinding',
    },
    'included_in': set(),
    'input_of': {
        'vkCreateDescriptorSetLayout',
        'vkGetDescriptorSetLayoutSupport',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DESCRIPTOR_SET_LAYOUT_CREATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkDescriptorSetLayoutCreateFlags'},
        'bindingCount': {'python_name': ['binding', 'count']},
        'pBindings': {'python_name': ['p', 'bindings'], 'len': [['bindingCount']], 'type': 'VkDescriptorSetLayoutBinding'},
    }
}
