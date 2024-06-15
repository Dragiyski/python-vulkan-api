import ctypes, sys

class VkVideoSessionCreateInfoKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkVideoSessionCreateInfoKHR

from . import VkVideoProfileInfoKHR
from . import VkExtensionProperties
from . import VkExtent2D

VkVideoSessionCreateInfoKHR._fields_ = [
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
