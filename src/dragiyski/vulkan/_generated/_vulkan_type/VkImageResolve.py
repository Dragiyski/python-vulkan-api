import ctypes

class VkImageResolve(ctypes.Structure):
    pass

from .VkExtent3D import VkExtent3D
from .VkImageSubresourceLayers import VkImageSubresourceLayers
from .VkOffset3D import VkOffset3D

VkImageResolve._fields_ = [
    ('srcSubresource', VkImageSubresourceLayers),
    ('srcOffset', VkOffset3D),
    ('dstSubresource', VkImageSubresourceLayers),
    ('dstOffset', VkOffset3D),
    ('extent', VkExtent3D),
]

VkImageResolve._type_ = {
    'srcSubresource': VkImageSubresourceLayers,
    'srcOffset': VkOffset3D,
    'dstSubresource': VkImageSubresourceLayers,
    'dstOffset': VkOffset3D,
    'extent': VkExtent3D,
}
