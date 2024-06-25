import ctypes

class VkSparseImageFormatProperties(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'aspectMask': ctypes.c_uint32,
            'imageGranularity': VkExtent3D,
            'flags': ctypes.c_uint32,
        }


from .VkExtent3D import VkExtent3D

VkSparseImageFormatProperties._fields_ = [
    ('aspectMask', ctypes.c_uint32),
    ('imageGranularity', VkExtent3D),
    ('flags', ctypes.c_uint32),
]
