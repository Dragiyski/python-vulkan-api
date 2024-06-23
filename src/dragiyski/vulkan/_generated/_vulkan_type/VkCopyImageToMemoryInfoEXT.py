import ctypes

class CType(ctypes.Structure):
    pass

from .VkImageToMemoryCopyEXT import CType as VkImageToMemoryCopyEXT

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('srcImage', ctypes.c_void_p),
    ('srcImageLayout', ctypes.c_int),
    ('regionCount', ctypes.c_uint32),
    ('pRegions', ctypes.POINTER(VkImageToMemoryCopyEXT)),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkImageToMemoryCopyEXT',
    },
    'included_in': set(),
    'input_of': {
        'vkCopyImageToMemoryEXT',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_COPY_IMAGE_TO_MEMORY_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkHostImageCopyFlagsEXT'},
        'srcImage': {'python_name': ['src', 'image']},
        'srcImageLayout': {'python_name': ['src', 'image', 'layout'], 'type': 'VkImageLayout'},
        'regionCount': {'python_name': ['region', 'count']},
        'pRegions': {'python_name': ['p', 'regions'], 'len': [['regionCount']], 'type': 'VkImageToMemoryCopyEXT'},
    }
}
