import ctypes

class VkImageBlit(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'srcSubresource': VkImageSubresourceLayers,
            'srcOffsets': ctypes.ARRAY(VkOffset3D, 2),
            'dstSubresource': VkImageSubresourceLayers,
            'dstOffsets': ctypes.ARRAY(VkOffset3D, 2),
        }


from .VkImageSubresourceLayers import VkImageSubresourceLayers
from .VkOffset3D import VkOffset3D

VkImageBlit._fields_ = [
    ('srcSubresource', VkImageSubresourceLayers),
    ('srcOffsets', ctypes.ARRAY(VkOffset3D, 2)),
    ('dstSubresource', VkImageSubresourceLayers),
    ('dstOffsets', ctypes.ARRAY(VkOffset3D, 2)),
]
