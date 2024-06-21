import ctypes

class CType(ctypes.Structure):
    pass

from .VkSparseImageFormatProperties import CType as VkSparseImageFormatProperties

CType._fields_ = [
    ('formatProperties', VkSparseImageFormatProperties),
    ('imageMipTailFirstLod', ctypes.c_uint32),
    ('imageMipTailSize', ctypes.c_uint64),
    ('imageMipTailOffset', ctypes.c_uint64),
    ('imageMipTailStride', ctypes.c_uint64),
]
