import ctypes

class VkSparseImageOpaqueMemoryBindInfo(ctypes.Structure):
    pass

from .VkSparseMemoryBind import VkSparseMemoryBind

VkSparseImageOpaqueMemoryBindInfo._fields_ = [
    ('image', ctypes.c_void_p),
    ('bindCount', ctypes.c_uint32),
    ('pBinds', ctypes.POINTER(VkSparseMemoryBind)),
]

VkSparseImageOpaqueMemoryBindInfo._type_ = {
    'image': ctypes.c_void_p,
    'bindCount': ctypes.c_uint32,
    'pBinds': ctypes.POINTER(VkSparseMemoryBind),
}
