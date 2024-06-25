import ctypes

class VkSparseBufferMemoryBindInfo(ctypes.Structure):
    pass

from .VkSparseMemoryBind import VkSparseMemoryBind

VkSparseBufferMemoryBindInfo._fields_ = [
    ('buffer', ctypes.c_void_p),
    ('bindCount', ctypes.c_uint32),
    ('pBinds', ctypes.POINTER(VkSparseMemoryBind)),
]

VkSparseBufferMemoryBindInfo._type_ = {
    'buffer': ctypes.c_void_p,
    'bindCount': ctypes.c_uint32,
    'pBinds': ctypes.POINTER(VkSparseMemoryBind),
}
