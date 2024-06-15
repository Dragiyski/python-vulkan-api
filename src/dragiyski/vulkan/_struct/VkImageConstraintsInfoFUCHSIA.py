import ctypes, sys

class VkImageConstraintsInfoFUCHSIA(ctypes.Structure):
    pass

sys.modules[__name__] = VkImageConstraintsInfoFUCHSIA

from . import VkImageFormatConstraintsInfoFUCHSIA
from . import VkBufferCollectionConstraintsInfoFUCHSIA

VkImageConstraintsInfoFUCHSIA._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('formatConstraintsCount', ctypes.c_uint32),
    ('pFormatConstraints', ctypes.POINTER(VkImageFormatConstraintsInfoFUCHSIA)),
    ('bufferCollectionConstraints', VkBufferCollectionConstraintsInfoFUCHSIA),
    ('flags', ctypes.c_uint32),
]
