import ctypes

class VkImageConstraintsInfoFUCHSIA(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'formatConstraintsCount': ctypes.c_uint32,
            'pFormatConstraints': ctypes.POINTER(VkImageFormatConstraintsInfoFUCHSIA),
            'bufferCollectionConstraints': VkBufferCollectionConstraintsInfoFUCHSIA,
            'flags': ctypes.c_uint32,
        }


from .VkBufferCollectionConstraintsInfoFUCHSIA import VkBufferCollectionConstraintsInfoFUCHSIA
from .VkImageFormatConstraintsInfoFUCHSIA import VkImageFormatConstraintsInfoFUCHSIA

VkImageConstraintsInfoFUCHSIA._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('formatConstraintsCount', ctypes.c_uint32),
    ('pFormatConstraints', ctypes.POINTER(VkImageFormatConstraintsInfoFUCHSIA)),
    ('bufferCollectionConstraints', VkBufferCollectionConstraintsInfoFUCHSIA),
    ('flags', ctypes.c_uint32),
]
