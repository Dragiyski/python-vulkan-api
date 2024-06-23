import ctypes

class CType(ctypes.Structure):
    pass

from .VkSparseMemoryBind import CType as VkSparseMemoryBind

CType._fields_ = [
    ('buffer', ctypes.c_void_p),
    ('bindCount', ctypes.c_uint32),
    ('pBinds', ctypes.POINTER(VkSparseMemoryBind)),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkSparseMemoryBind',
    },
    'included_in': {
        'VkBindSparseInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'buffer': {'python_name': ['buffer']},
        'bindCount': {'python_name': ['bind', 'count']},
        'pBinds': {'python_name': ['p', 'binds'], 'len': [['bindCount']], 'type': 'VkSparseMemoryBind'},
    }
}
