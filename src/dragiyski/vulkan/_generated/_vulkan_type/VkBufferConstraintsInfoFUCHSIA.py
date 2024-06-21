import ctypes

class CType(ctypes.Structure):
    pass

from .VkBufferCollectionConstraintsInfoFUCHSIA import CType as VkBufferCollectionConstraintsInfoFUCHSIA
from .VkBufferCreateInfo import CType as VkBufferCreateInfo

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('createInfo', VkBufferCreateInfo),
    ('requiredFormatFeatures', ctypes.c_uint32),
    ('bufferCollectionConstraints', VkBufferCollectionConstraintsInfoFUCHSIA),
]
