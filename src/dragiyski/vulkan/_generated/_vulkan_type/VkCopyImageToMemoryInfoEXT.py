import ctypes

class VkCopyImageToMemoryInfoEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'flags': ctypes.c_uint32,
            'srcImage': ctypes.c_void_p,
            'srcImageLayout': ctypes.c_int,
            'regionCount': ctypes.c_uint32,
            'pRegions': ctypes.POINTER(VkImageToMemoryCopyEXT),
        }


from .VkImageToMemoryCopyEXT import VkImageToMemoryCopyEXT

VkCopyImageToMemoryInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('srcImage', ctypes.c_void_p),
    ('srcImageLayout', ctypes.c_int),
    ('regionCount', ctypes.c_uint32),
    ('pRegions', ctypes.POINTER(VkImageToMemoryCopyEXT)),
]
