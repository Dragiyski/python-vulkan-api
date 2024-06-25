import ctypes

class VkImageBlit2(ctypes.Structure):
    pass

from .VkImageSubresourceLayers import VkImageSubresourceLayers
from .VkOffset3D import VkOffset3D

VkImageBlit2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('srcSubresource', VkImageSubresourceLayers),
    ('srcOffsets', ctypes.ARRAY(VkOffset3D, 2)),
    ('dstSubresource', VkImageSubresourceLayers),
    ('dstOffsets', ctypes.ARRAY(VkOffset3D, 2)),
]

VkImageBlit2._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'srcSubresource': VkImageSubresourceLayers,
    'srcOffsets': ctypes.ARRAY(VkOffset3D, 2),
    'dstSubresource': VkImageSubresourceLayers,
    'dstOffsets': ctypes.ARRAY(VkOffset3D, 2),
}
