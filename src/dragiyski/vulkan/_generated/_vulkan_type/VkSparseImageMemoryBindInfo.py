import ctypes, sys

class VkSparseImageMemoryBindInfo(ctypes.Structure):
    pass

sys.modules[__name__] = VkSparseImageMemoryBindInfo

from . import VkSparseImageMemoryBind

VkSparseImageMemoryBindInfo._fields_ = [
    ('image', ctypes.c_void_p),
    ('bindCount', ctypes.c_uint32),
    ('pBinds', ctypes.POINTER(VkSparseImageMemoryBind)),
]
