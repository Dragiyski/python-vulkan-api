import ctypes

class CType(ctypes.Structure):
    pass

from .VkBufferImageCopy2 import CType as VkBufferImageCopy2

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('srcImage', ctypes.c_void_p),
    ('srcImageLayout', ctypes.c_int),
    ('dstBuffer', ctypes.c_void_p),
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
        'vkCmdCopyImageToBuffer2',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_COPY_IMAGE_TO_BUFFER_INFO_2', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'srcImage': {'python_name': ['src', 'image']},
        'srcImageLayout': {'python_name': ['src', 'image', 'layout'], 'type': 'VkImageLayout'},
        'dstBuffer': {'python_name': ['dst', 'buffer']},
        'regionCount': {'python_name': ['region', 'count']},
        'pRegions': {'python_name': ['p', 'regions'], 'len': [['regionCount']], 'type': 'VkBufferImageCopy2'},
    }
}
