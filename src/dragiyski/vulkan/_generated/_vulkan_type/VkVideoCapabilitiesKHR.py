import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtensionProperties import CType as VkExtensionProperties
from .VkExtent2D import CType as VkExtent2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('minBitstreamBufferOffsetAlignment', ctypes.c_uint64),
    ('minBitstreamBufferSizeAlignment', ctypes.c_uint64),
    ('pictureAccessGranularity', VkExtent2D),
    ('minCodedExtent', VkExtent2D),
    ('maxCodedExtent', VkExtent2D),
    ('maxDpbSlots', ctypes.c_uint32),
    ('maxActiveReferencePictures', ctypes.c_uint32),
    ('stdHeaderVersion', VkExtensionProperties),
]
