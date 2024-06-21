import ctypes

class CType(ctypes.Structure):
    pass

from .VkSparseImageMemoryBind import CType as VkSparseImageMemoryBind

CType._fields_ = [
    ('image', ctypes.c_void_p),
    ('bindCount', ctypes.c_uint32),
    ('pBinds', ctypes.POINTER(VkSparseImageMemoryBind)),
]
