import ctypes

class VkCopyImageToImageInfoEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'flags': ctypes.c_uint32,
            'srcImage': ctypes.c_void_p,
            'srcImageLayout': ctypes.c_int,
            'dstImage': ctypes.c_void_p,
            'dstImageLayout': ctypes.c_int,
            'regionCount': ctypes.c_uint32,
            'pRegions': ctypes.POINTER(VkImageCopy2),
        }


from .VkImageCopy2 import VkImageCopy2

VkCopyImageToImageInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('srcImage', ctypes.c_void_p),
    ('srcImageLayout', ctypes.c_int),
    ('dstImage', ctypes.c_void_p),
    ('dstImageLayout', ctypes.c_int),
    ('regionCount', ctypes.c_uint32),
    ('pRegions', ctypes.POINTER(VkImageCopy2)),
]
