import ctypes

class CType(ctypes.Structure):
    pass

from .VkBufferCollectionConstraintsInfoFUCHSIA import CType as VkBufferCollectionConstraintsInfoFUCHSIA
from .VkImageFormatConstraintsInfoFUCHSIA import CType as VkImageFormatConstraintsInfoFUCHSIA

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('formatConstraintsCount', ctypes.c_uint32),
    ('pFormatConstraints', ctypes.POINTER(VkImageFormatConstraintsInfoFUCHSIA)),
    ('bufferCollectionConstraints', VkBufferCollectionConstraintsInfoFUCHSIA),
    ('flags', ctypes.c_uint32),
]
