import ctypes

class VkSparseBufferMemoryBindInfo(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'buffer': ctypes.c_void_p,
            'bindCount': ctypes.c_uint32,
            'pBinds': ctypes.POINTER(VkSparseMemoryBind),
        }


from .VkSparseMemoryBind import VkSparseMemoryBind

VkSparseBufferMemoryBindInfo._fields_ = [
    ('buffer', ctypes.c_void_p),
    ('bindCount', ctypes.c_uint32),
    ('pBinds', ctypes.POINTER(VkSparseMemoryBind)),
]
