import ctypes

class CType(ctypes.Structure):
    pass

from .VkMutableDescriptorTypeListEXT import CType as VkMutableDescriptorTypeListEXT

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('mutableDescriptorTypeListCount', ctypes.c_uint32),
    ('pMutableDescriptorTypeLists', ctypes.POINTER(VkMutableDescriptorTypeListEXT)),
]

descriptor = {
    'extends': {
        'VkDescriptorPoolCreateInfo',
        'VkDescriptorSetLayoutCreateInfo',
    },
    'extended_by': set(),
    'includes': {
        'VkMutableDescriptorTypeListEXT',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_MUTABLE_DESCRIPTOR_TYPE_CREATE_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'mutableDescriptorTypeListCount': {'python_name': ['mutable', 'descriptor', 'type', 'list', 'count']},
        'pMutableDescriptorTypeLists': {'python_name': ['p', 'mutable', 'descriptor', 'type', 'lists'], 'len': [['mutableDescriptorTypeListCount']], 'type': 'VkMutableDescriptorTypeListEXT'},
    }
}
