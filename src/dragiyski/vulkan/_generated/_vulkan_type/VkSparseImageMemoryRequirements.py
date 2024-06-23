import ctypes

class CType(ctypes.Structure):
    pass

from .VkSparseImageFormatProperties import CType as VkSparseImageFormatProperties

CType._fields_ = [
    ('formatProperties', VkSparseImageFormatProperties),
    ('imageMipTailFirstLod', ctypes.c_uint32),
    ('imageMipTailSize', ctypes.c_uint64),
    ('imageMipTailOffset', ctypes.c_uint64),
    ('imageMipTailStride', ctypes.c_uint64),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkSparseImageFormatProperties',
    },
    'included_in': {
        'VkSparseImageMemoryRequirements2',
    },
    'input_of': set(),
    'output_of': {
        'vkGetImageSparseMemoryRequirements',
    },
    'member_map': {
        'formatProperties': {'python_name': ['format', 'properties'], 'type': 'VkSparseImageFormatProperties'},
        'imageMipTailFirstLod': {'python_name': ['image', 'mip', 'tail', 'first', 'lod']},
        'imageMipTailSize': {'python_name': ['image', 'mip', 'tail', 'size']},
        'imageMipTailOffset': {'python_name': ['image', 'mip', 'tail', 'offset']},
        'imageMipTailStride': {'python_name': ['image', 'mip', 'tail', 'stride']},
    }
}
