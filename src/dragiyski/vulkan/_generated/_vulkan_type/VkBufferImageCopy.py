import ctypes

class VkBufferImageCopy(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'bufferOffset': ctypes.c_uint64,
            'bufferRowLength': ctypes.c_uint32,
            'bufferImageHeight': ctypes.c_uint32,
            'imageSubresource': VkImageSubresourceLayers,
            'imageOffset': VkOffset3D,
            'imageExtent': VkExtent3D,
        }


from .VkExtent3D import VkExtent3D
from .VkImageSubresourceLayers import VkImageSubresourceLayers
from .VkOffset3D import VkOffset3D

VkBufferImageCopy._fields_ = [
    ('bufferOffset', ctypes.c_uint64),
    ('bufferRowLength', ctypes.c_uint32),
    ('bufferImageHeight', ctypes.c_uint32),
    ('imageSubresource', VkImageSubresourceLayers),
    ('imageOffset', VkOffset3D),
    ('imageExtent', VkExtent3D),
]
