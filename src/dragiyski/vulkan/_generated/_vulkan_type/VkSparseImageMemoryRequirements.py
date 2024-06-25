import ctypes

class VkSparseImageMemoryRequirements(ctypes.Structure):
    pass

from .VkSparseImageFormatProperties import VkSparseImageFormatProperties

VkSparseImageMemoryRequirements._fields_ = [
    ('formatProperties', VkSparseImageFormatProperties),
    ('imageMipTailFirstLod', ctypes.c_uint32),
    ('imageMipTailSize', ctypes.c_uint64),
    ('imageMipTailOffset', ctypes.c_uint64),
    ('imageMipTailStride', ctypes.c_uint64),
]

VkSparseImageMemoryRequirements._type_ = {
    'formatProperties': VkSparseImageFormatProperties,
    'imageMipTailFirstLod': ctypes.c_uint32,
    'imageMipTailSize': ctypes.c_uint64,
    'imageMipTailOffset': ctypes.c_uint64,
    'imageMipTailStride': ctypes.c_uint64,
}
