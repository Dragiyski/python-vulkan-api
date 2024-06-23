import ctypes

class CType(ctypes.Structure):
    pass

from .VkSparseImageFormatProperties import CType as VkSparseImageFormatProperties

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('properties', VkSparseImageFormatProperties),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkSparseImageFormatProperties',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetPhysicalDeviceSparseImageFormatProperties2',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_SPARSE_IMAGE_FORMAT_PROPERTIES_2', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'properties': {'python_name': ['properties'], 'type': 'VkSparseImageFormatProperties'},
    }
}
