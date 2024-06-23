import ctypes

class CType(ctypes.Structure):
    pass

from .VkImageCopy2 import CType as VkImageCopy2

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('srcImage', ctypes.c_void_p),
    ('srcImageLayout', ctypes.c_int),
    ('dstImage', ctypes.c_void_p),
    ('dstImageLayout', ctypes.c_int),
    ('regionCount', ctypes.c_uint32),
    ('pRegions', ctypes.POINTER(VkImageCopy2)),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkImageCopy2',
    },
    'included_in': set(),
    'input_of': {
        'vkCopyImageToImageEXT',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_COPY_IMAGE_TO_IMAGE_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkHostImageCopyFlagsEXT'},
        'srcImage': {'python_name': ['src', 'image']},
        'srcImageLayout': {'python_name': ['src', 'image', 'layout'], 'type': 'VkImageLayout'},
        'dstImage': {'python_name': ['dst', 'image']},
        'dstImageLayout': {'python_name': ['dst', 'image', 'layout'], 'type': 'VkImageLayout'},
        'regionCount': {'python_name': ['region', 'count']},
        'pRegions': {'python_name': ['p', 'regions'], 'len': [['regionCount']], 'type': 'VkImageCopy2'},
    }
}
