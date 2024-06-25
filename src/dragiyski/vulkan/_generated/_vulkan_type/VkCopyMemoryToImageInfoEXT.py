import ctypes

class VkCopyMemoryToImageInfoEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'flags': ctypes.c_uint32,
            'dstImage': ctypes.c_void_p,
            'dstImageLayout': ctypes.c_int,
            'regionCount': ctypes.c_uint32,
            'pRegions': ctypes.POINTER(VkMemoryToImageCopyEXT),
        }


from .VkMemoryToImageCopyEXT import VkMemoryToImageCopyEXT

VkCopyMemoryToImageInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('dstImage', ctypes.c_void_p),
    ('dstImageLayout', ctypes.c_int),
    ('regionCount', ctypes.c_uint32),
    ('pRegions', ctypes.POINTER(VkMemoryToImageCopyEXT)),
]
