import ctypes

class VkVideoSessionCreateInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'queueFamilyIndex': ctypes.c_uint32,
            'flags': ctypes.c_uint32,
            'pVideoProfile': ctypes.POINTER(VkVideoProfileInfoKHR),
            'pictureFormat': ctypes.c_int,
            'maxCodedExtent': VkExtent2D,
            'referencePictureFormat': ctypes.c_int,
            'maxDpbSlots': ctypes.c_uint32,
            'maxActiveReferencePictures': ctypes.c_uint32,
            'pStdHeaderVersion': ctypes.POINTER(VkExtensionProperties),
        }


from .VkExtensionProperties import VkExtensionProperties
from .VkExtent2D import VkExtent2D
from .VkVideoProfileInfoKHR import VkVideoProfileInfoKHR

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
