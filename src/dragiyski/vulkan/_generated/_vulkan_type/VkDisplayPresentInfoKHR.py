import ctypes

class CType(ctypes.Structure):
    pass

from .VkRect2D import CType as VkRect2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('srcRect', VkRect2D),
    ('dstRect', VkRect2D),
    ('persistent', ctypes.c_uint32),
]

descriptor = {
    'extends': {
        'VkPresentInfoKHR',
    },
    'extended_by': set(),
    'includes': {
        'VkRect2D',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DISPLAY_PRESENT_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'srcRect': {'python_name': ['src', 'rect'], 'type': 'VkRect2D'},
        'dstRect': {'python_name': ['dst', 'rect'], 'type': 'VkRect2D'},
        'persistent': {'python_name': ['persistent']},
    }
}
