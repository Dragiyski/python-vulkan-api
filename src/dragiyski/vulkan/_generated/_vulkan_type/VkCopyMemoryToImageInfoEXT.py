import ctypes

class CType(ctypes.Structure):
    pass

from .VkMemoryToImageCopyEXT import CType as VkMemoryToImageCopyEXT

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('dstImage', ctypes.c_void_p),
    ('dstImageLayout', ctypes.c_int),
    ('regionCount', ctypes.c_uint32),
    ('pRegions', ctypes.POINTER(VkMemoryToImageCopyEXT)),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkMemoryToImageCopyEXT',
    },
    'included_in': set(),
    'input_of': {
        'vkCopyMemoryToImageEXT',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_COPY_MEMORY_TO_IMAGE_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkHostImageCopyFlagsEXT'},
        'dstImage': {'python_name': ['dst', 'image']},
        'dstImageLayout': {'python_name': ['dst', 'image', 'layout'], 'type': 'VkImageLayout'},
        'regionCount': {'python_name': ['region', 'count']},
        'pRegions': {'python_name': ['p', 'regions'], 'len': [['regionCount']], 'type': 'VkMemoryToImageCopyEXT'},
    }
}
