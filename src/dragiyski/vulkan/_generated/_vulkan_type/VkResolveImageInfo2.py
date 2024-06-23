import ctypes

class CType(ctypes.Structure):
    pass

from .VkImageResolve2 import CType as VkImageResolve2

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('srcImage', ctypes.c_void_p),
    ('srcImageLayout', ctypes.c_int),
    ('dstImage', ctypes.c_void_p),
    ('dstImageLayout', ctypes.c_int),
    ('regionCount', ctypes.c_uint32),
    ('pRegions', ctypes.POINTER(VkImageResolve2)),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkImageResolve2',
    },
    'included_in': set(),
    'input_of': {
        'vkCmdResolveImage2',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_RESOLVE_IMAGE_INFO_2', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'srcImage': {'python_name': ['src', 'image']},
        'srcImageLayout': {'python_name': ['src', 'image', 'layout'], 'type': 'VkImageLayout'},
        'dstImage': {'python_name': ['dst', 'image']},
        'dstImageLayout': {'python_name': ['dst', 'image', 'layout'], 'type': 'VkImageLayout'},
        'regionCount': {'python_name': ['region', 'count']},
        'pRegions': {'python_name': ['p', 'regions'], 'len': [['regionCount']], 'type': 'VkImageResolve2'},
    }
}
