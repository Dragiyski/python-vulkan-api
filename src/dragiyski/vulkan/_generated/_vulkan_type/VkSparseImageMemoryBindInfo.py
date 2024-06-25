import ctypes

class VkSparseImageMemoryBindInfo(ctypes.Structure):
    pass

from .VkSparseImageMemoryBind import VkSparseImageMemoryBind

VkSparseImageMemoryBindInfo._fields_ = [
    ('image', ctypes.c_void_p),
    ('bindCount', ctypes.c_uint32),
    ('pBinds', ctypes.POINTER(VkSparseImageMemoryBind)),
]

VkSparseImageMemoryBindInfo._type_ = {
    'image': ctypes.c_void_p,
    'bindCount': ctypes.c_uint32,
    'pBinds': ctypes.POINTER(VkSparseImageMemoryBind),
}
