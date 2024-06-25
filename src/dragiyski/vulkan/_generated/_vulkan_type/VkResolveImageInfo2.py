import ctypes

class VkResolveImageInfo2(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'srcImage': ctypes.c_void_p,
            'srcImageLayout': ctypes.c_int,
            'dstImage': ctypes.c_void_p,
            'dstImageLayout': ctypes.c_int,
            'regionCount': ctypes.c_uint32,
            'pRegions': ctypes.POINTER(VkImageResolve2),
        }


from .VkImageResolve2 import VkImageResolve2

VkResolveImageInfo2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('srcImage', ctypes.c_void_p),
    ('srcImageLayout', ctypes.c_int),
    ('dstImage', ctypes.c_void_p),
    ('dstImageLayout', ctypes.c_int),
    ('regionCount', ctypes.c_uint32),
    ('pRegions', ctypes.POINTER(VkImageResolve2)),
]
