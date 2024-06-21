import ctypes

class CType(ctypes.Structure):
    pass

from .VkSparseMemoryBind import CType as VkSparseMemoryBind

CType._fields_ = [
    ('buffer', ctypes.c_void_p),
    ('bindCount', ctypes.c_uint32),
    ('pBinds', ctypes.POINTER(VkSparseMemoryBind)),
]
