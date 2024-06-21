import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtensionProperties import CType as VkExtensionProperties
from .VkExtent2D import CType as VkExtent2D
from .VkVideoProfileInfoKHR import CType as VkVideoProfileInfoKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('queueFamilyIndex', ctypes.c_uint32),
    ('flags', ctypes.c_uint32),
    ('pVideoProfile', ctypes.POINTER(VkVideoProfileInfoKHR)),
    ('pictureFormat', ctypes.c_int),
    ('maxCodedExtent', VkExtent2D),
    ('referencePictureFormat', ctypes.c_int),
    ('maxDpbSlots', ctypes.c_uint32),
    ('maxActiveReferencePictures', ctypes.c_uint32),
    ('pStdHeaderVersion', ctypes.POINTER(VkExtensionProperties)),
]
