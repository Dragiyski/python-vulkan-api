import ctypes

class CType(ctypes.Structure):
    pass

from .VkBufferImageCopy2 import CType as VkBufferImageCopy2

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('srcBuffer', ctypes.c_void_p),
    ('dstImage', ctypes.c_void_p),
    ('dstImageLayout', ctypes.c_int),
    ('regionCount', ctypes.c_uint32),
    ('pRegions', ctypes.POINTER(VkBufferImageCopy2)),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkBufferImageCopy2',
    },
    'included_in': set(),
    'input_of': {
        'vkCmdCopyBufferToImage2',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_COPY_BUFFER_TO_IMAGE_INFO_2', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'srcBuffer': {'python_name': ['src', 'buffer']},
        'dstImage': {'python_name': ['dst', 'image']},
        'dstImageLayout': {'python_name': ['dst', 'image', 'layout'], 'type': 'VkImageLayout'},
        'regionCount': {'python_name': ['region', 'count']},
        'pRegions': {'python_name': ['p', 'regions'], 'len': [['regionCount']], 'type': 'VkBufferImageCopy2'},
    }
}
