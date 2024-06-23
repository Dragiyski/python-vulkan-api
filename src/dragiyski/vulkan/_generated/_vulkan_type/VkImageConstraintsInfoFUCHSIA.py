import ctypes

class CType(ctypes.Structure):
    pass

from .VkBufferCollectionConstraintsInfoFUCHSIA import CType as VkBufferCollectionConstraintsInfoFUCHSIA
from .VkImageFormatConstraintsInfoFUCHSIA import CType as VkImageFormatConstraintsInfoFUCHSIA

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('formatConstraintsCount', ctypes.c_uint32),
    ('pFormatConstraints', ctypes.POINTER(VkImageFormatConstraintsInfoFUCHSIA)),
    ('bufferCollectionConstraints', VkBufferCollectionConstraintsInfoFUCHSIA),
    ('flags', ctypes.c_uint32),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkBufferCollectionConstraintsInfoFUCHSIA',
        'VkImageFormatConstraintsInfoFUCHSIA',
    },
    'included_in': set(),
    'input_of': {
        'vkSetBufferCollectionImageConstraintsFUCHSIA',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_IMAGE_CONSTRAINTS_INFO_FUCHSIA', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'formatConstraintsCount': {'python_name': ['format', 'constraints', 'count']},
        'pFormatConstraints': {'python_name': ['p', 'format', 'constraints'], 'len': [['formatConstraintsCount']], 'type': 'VkImageFormatConstraintsInfoFUCHSIA'},
        'bufferCollectionConstraints': {'python_name': ['buffer', 'collection', 'constraints'], 'type': 'VkBufferCollectionConstraintsInfoFUCHSIA'},
        'flags': {'python_name': ['flags'], 'type': 'VkImageConstraintsInfoFlagsFUCHSIA'},
    }
}
