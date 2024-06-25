import ctypes

class VkImageFormatProperties(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'maxExtent': VkExtent3D,
            'maxMipLevels': ctypes.c_uint32,
            'maxArrayLayers': ctypes.c_uint32,
            'sampleCounts': ctypes.c_uint32,
            'maxResourceSize': ctypes.c_uint64,
        }


from .VkExtent3D import VkExtent3D

VkImageFormatProperties._fields_ = [
    ('maxExtent', VkExtent3D),
    ('maxMipLevels', ctypes.c_uint32),
    ('maxArrayLayers', ctypes.c_uint32),
    ('sampleCounts', ctypes.c_uint32),
    ('maxResourceSize', ctypes.c_uint64),
]
