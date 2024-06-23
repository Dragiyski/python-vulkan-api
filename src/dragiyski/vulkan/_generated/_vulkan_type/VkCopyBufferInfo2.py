import ctypes

class CType(ctypes.Structure):
    pass

from .VkBufferCopy2 import CType as VkBufferCopy2

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('srcBuffer', ctypes.c_void_p),
    ('dstBuffer', ctypes.c_void_p),
    ('regionCount', ctypes.c_uint32),
    ('pRegions', ctypes.POINTER(VkBufferCopy2)),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkBufferCopy2',
    },
    'included_in': set(),
    'input_of': {
        'vkCmdCopyBuffer2',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_COPY_BUFFER_INFO_2', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'srcBuffer': {'python_name': ['src', 'buffer']},
        'dstBuffer': {'python_name': ['dst', 'buffer']},
        'regionCount': {'python_name': ['region', 'count']},
        'pRegions': {'python_name': ['p', 'regions'], 'len': [['regionCount']], 'type': 'VkBufferCopy2'},
    }
}
