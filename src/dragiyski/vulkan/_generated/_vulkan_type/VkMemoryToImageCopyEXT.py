import ctypes

class VkMemoryToImageCopyEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'pHostPointer': ctypes.c_void_p,
            'memoryRowLength': ctypes.c_uint32,
            'memoryImageHeight': ctypes.c_uint32,
            'imageSubresource': VkImageSubresourceLayers,
            'imageOffset': VkOffset3D,
            'imageExtent': VkExtent3D,
        }


from .VkExtent3D import VkExtent3D
from .VkImageSubresourceLayers import VkImageSubresourceLayers
from .VkOffset3D import VkOffset3D

VkMemoryToImageCopyEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pHostPointer', ctypes.c_void_p),
    ('memoryRowLength', ctypes.c_uint32),
    ('memoryImageHeight', ctypes.c_uint32),
    ('imageSubresource', VkImageSubresourceLayers),
    ('imageOffset', VkOffset3D),
    ('imageExtent', VkExtent3D),
]
