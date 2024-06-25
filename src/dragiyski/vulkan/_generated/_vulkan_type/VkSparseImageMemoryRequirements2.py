import ctypes

class VkSparseImageMemoryRequirements2(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'memoryRequirements': VkSparseImageMemoryRequirements,
        }


from .VkSparseImageMemoryRequirements import VkSparseImageMemoryRequirements

VkSparseImageMemoryRequirements2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('memoryRequirements', VkSparseImageMemoryRequirements),
]
