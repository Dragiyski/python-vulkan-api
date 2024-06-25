import ctypes

class VkSparseImageMemoryBindInfo(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'image': ctypes.c_void_p,
            'bindCount': ctypes.c_uint32,
            'pBinds': ctypes.POINTER(VkSparseImageMemoryBind),
        }


from .VkSparseImageMemoryBind import VkSparseImageMemoryBind

VkSparseImageMemoryBindInfo._fields_ = [
    ('image', ctypes.c_void_p),
    ('bindCount', ctypes.c_uint32),
    ('pBinds', ctypes.POINTER(VkSparseImageMemoryBind)),
]
