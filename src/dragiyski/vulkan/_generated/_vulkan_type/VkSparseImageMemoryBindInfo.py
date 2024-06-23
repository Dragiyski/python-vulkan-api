import ctypes

class CType(ctypes.Structure):
    pass

from .VkSparseImageMemoryBind import CType as VkSparseImageMemoryBind

CType._fields_ = [
    ('image', ctypes.c_void_p),
    ('bindCount', ctypes.c_uint32),
    ('pBinds', ctypes.POINTER(VkSparseImageMemoryBind)),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkSparseImageMemoryBind',
    },
    'included_in': {
        'VkBindSparseInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'image': {'python_name': ['image']},
        'bindCount': {'python_name': ['bind', 'count']},
        'pBinds': {'python_name': ['p', 'binds'], 'len': [['bindCount']], 'type': 'VkSparseImageMemoryBind'},
    }
}
