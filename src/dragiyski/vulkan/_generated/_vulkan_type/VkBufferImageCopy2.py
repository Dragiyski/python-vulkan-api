import ctypes

class VkBufferImageCopy2(ctypes.Structure):
    pass

from .VkExtent3D import VkExtent3D
from .VkImageSubresourceLayers import VkImageSubresourceLayers
from .VkOffset3D import VkOffset3D

VkBufferImageCopy2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('bufferOffset', ctypes.c_uint64),
    ('bufferRowLength', ctypes.c_uint32),
    ('bufferImageHeight', ctypes.c_uint32),
    ('imageSubresource', VkImageSubresourceLayers),
    ('imageOffset', VkOffset3D),
    ('imageExtent', VkExtent3D),
]

VkBufferImageCopy2._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'bufferOffset': ctypes.c_uint64,
    'bufferRowLength': ctypes.c_uint32,
    'bufferImageHeight': ctypes.c_uint32,
    'imageSubresource': VkImageSubresourceLayers,
    'imageOffset': VkOffset3D,
    'imageExtent': VkExtent3D,
}
