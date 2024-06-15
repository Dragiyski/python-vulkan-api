import ctypes, sys

class VkBufferConstraintsInfoFUCHSIA(ctypes.Structure):
    pass

sys.modules[__name__] = VkBufferConstraintsInfoFUCHSIA

from . import VkBufferCollectionConstraintsInfoFUCHSIA
from . import VkBufferCreateInfo

VkBufferConstraintsInfoFUCHSIA._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('createInfo', VkBufferCreateInfo),
    ('requiredFormatFeatures', ctypes.c_uint32),
    ('bufferCollectionConstraints', VkBufferCollectionConstraintsInfoFUCHSIA),
]
