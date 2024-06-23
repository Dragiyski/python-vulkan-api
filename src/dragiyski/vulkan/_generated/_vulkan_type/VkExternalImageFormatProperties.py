import ctypes

class CType(ctypes.Structure):
    pass

from .VkExternalMemoryProperties import CType as VkExternalMemoryProperties

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('externalMemoryProperties', VkExternalMemoryProperties),
]

descriptor = {
    'extends': {
        'VkImageFormatProperties2',
    },
    'extended_by': set(),
    'includes': {
        'VkExternalMemoryProperties',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_EXTERNAL_IMAGE_FORMAT_PROPERTIES', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'externalMemoryProperties': {'python_name': ['external', 'memory', 'properties'], 'type': 'VkExternalMemoryProperties'},
    }
}
