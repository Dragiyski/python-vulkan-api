import ctypes

class VkBufferConstraintsInfoFUCHSIA(ctypes.Structure):
    pass

from .VkBufferCollectionConstraintsInfoFUCHSIA import VkBufferCollectionConstraintsInfoFUCHSIA
from .VkBufferCreateInfo import VkBufferCreateInfo

VkBufferConstraintsInfoFUCHSIA._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('createInfo', VkBufferCreateInfo),
    ('requiredFormatFeatures', ctypes.c_uint32),
    ('bufferCollectionConstraints', VkBufferCollectionConstraintsInfoFUCHSIA),
]

VkBufferConstraintsInfoFUCHSIA._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'createInfo': VkBufferCreateInfo,
    'requiredFormatFeatures': ctypes.c_uint32,
    'bufferCollectionConstraints': VkBufferCollectionConstraintsInfoFUCHSIA,
}
