import ctypes, sys

class VkSparseBufferMemoryBindInfo(ctypes.Structure):
    pass

sys.modules[__name__] = VkSparseBufferMemoryBindInfo

from . import VkSparseMemoryBind

VkSparseBufferMemoryBindInfo._fields_ = [
    ('buffer', ctypes.c_void_p),
    ('bindCount', ctypes.c_uint32),
    ('pBinds', ctypes.POINTER(VkSparseMemoryBind)),
]
