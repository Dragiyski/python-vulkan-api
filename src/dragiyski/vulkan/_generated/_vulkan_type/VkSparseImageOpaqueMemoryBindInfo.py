import ctypes, sys

class VkSparseImageOpaqueMemoryBindInfo(ctypes.Structure):
    pass

sys.modules[__name__] = VkSparseImageOpaqueMemoryBindInfo

from . import VkSparseMemoryBind

VkSparseImageOpaqueMemoryBindInfo._fields_ = [
    ('image', ctypes.c_void_p),
    ('bindCount', ctypes.c_uint32),
    ('pBinds', ctypes.POINTER(VkSparseMemoryBind)),
]
