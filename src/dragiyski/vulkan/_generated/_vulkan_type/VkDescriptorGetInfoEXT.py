import ctypes

class CType(ctypes.Structure):
    pass

from .VkDescriptorDataEXT import CType as VkDescriptorDataEXT

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('type', ctypes.c_int),
    ('data', VkDescriptorDataEXT),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkDescriptorDataEXT',
    },
    'included_in': set(),
    'input_of': {
        'vkGetDescriptorEXT',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DESCRIPTOR_GET_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'type': {'python_name': ['type'], 'type': 'VkDescriptorType'},
        'data': {'python_name': ['data'], 'type': 'VkDescriptorDataEXT'},
    }
}
