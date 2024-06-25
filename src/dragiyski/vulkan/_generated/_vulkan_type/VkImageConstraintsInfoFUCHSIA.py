import ctypes

class VkImageConstraintsInfoFUCHSIA(ctypes.Structure):
    pass

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

VkImageConstraintsInfoFUCHSIA._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'formatConstraintsCount': ctypes.c_uint32,
    'pFormatConstraints': ctypes.POINTER(VkImageFormatConstraintsInfoFUCHSIA),
    'bufferCollectionConstraints': VkBufferCollectionConstraintsInfoFUCHSIA,
    'flags': ctypes.c_uint32,
}
