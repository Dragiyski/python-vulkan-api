import ctypes

class VkCopyMemoryToImageIndirectCommandNV(ctypes.Structure):
    pass

from .VkExtent3D import VkExtent3D
from .VkImageSubresourceLayers import VkImageSubresourceLayers
from .VkOffset3D import VkOffset3D

VkCopyMemoryToImageIndirectCommandNV._fields_ = [
    ('srcAddress', ctypes.c_uint64),
    ('bufferRowLength', ctypes.c_uint32),
    ('bufferImageHeight', ctypes.c_uint32),
    ('imageSubresource', VkImageSubresourceLayers),
    ('imageOffset', VkOffset3D),
    ('imageExtent', VkExtent3D),
]

VkCopyMemoryToImageIndirectCommandNV._type_ = {
    'srcAddress': ctypes.c_uint64,
    'bufferRowLength': ctypes.c_uint32,
    'bufferImageHeight': ctypes.c_uint32,
    'imageSubresource': VkImageSubresourceLayers,
    'imageOffset': VkOffset3D,
    'imageExtent': VkExtent3D,
}
