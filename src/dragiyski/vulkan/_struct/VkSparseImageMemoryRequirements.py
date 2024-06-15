import ctypes, sys

class VkSparseImageMemoryRequirements(ctypes.Structure):
    pass

sys.modules[__name__] = VkSparseImageMemoryRequirements

from . import VkSparseImageFormatProperties

VkSparseImageMemoryRequirements._fields_ = [
    ('formatProperties', VkSparseImageFormatProperties),
    ('imageMipTailFirstLod', ctypes.c_uint32),
    ('imageMipTailSize', ctypes.c_uint64),
    ('imageMipTailOffset', ctypes.c_uint64),
    ('imageMipTailStride', ctypes.c_uint64),
]
