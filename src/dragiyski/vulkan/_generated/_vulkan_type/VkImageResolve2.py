import ctypes

class VkImageResolve2(ctypes.Structure):
    pass

from .VkExtent3D import VkExtent3D
from .VkImageSubresourceLayers import VkImageSubresourceLayers
from .VkOffset3D import VkOffset3D

VkImageResolve2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('srcSubresource', VkImageSubresourceLayers),
    ('srcOffset', VkOffset3D),
    ('dstSubresource', VkImageSubresourceLayers),
    ('dstOffset', VkOffset3D),
    ('extent', VkExtent3D),
]

VkImageResolve2._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'srcSubresource': VkImageSubresourceLayers,
    'srcOffset': VkOffset3D,
    'dstSubresource': VkImageSubresourceLayers,
    'dstOffset': VkOffset3D,
    'extent': VkExtent3D,
}
