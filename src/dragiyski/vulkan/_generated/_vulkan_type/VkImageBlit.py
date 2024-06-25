import ctypes

class VkImageBlit(ctypes.Structure):
    pass

from .VkImageSubresourceLayers import VkImageSubresourceLayers
from .VkOffset3D import VkOffset3D

VkImageBlit._fields_ = [
    ('srcSubresource', VkImageSubresourceLayers),
    ('srcOffsets', ctypes.ARRAY(VkOffset3D, 2)),
    ('dstSubresource', VkImageSubresourceLayers),
    ('dstOffsets', ctypes.ARRAY(VkOffset3D, 2)),
]

VkImageBlit._type_ = {
    'srcSubresource': VkImageSubresourceLayers,
    'srcOffsets': ctypes.ARRAY(VkOffset3D, 2),
    'dstSubresource': VkImageSubresourceLayers,
    'dstOffsets': ctypes.ARRAY(VkOffset3D, 2),
}
