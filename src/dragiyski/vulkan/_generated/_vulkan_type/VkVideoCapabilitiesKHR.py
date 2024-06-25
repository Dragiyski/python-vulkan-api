import ctypes

class VkVideoCapabilitiesKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'flags': ctypes.c_uint32,
            'minBitstreamBufferOffsetAlignment': ctypes.c_uint64,
            'minBitstreamBufferSizeAlignment': ctypes.c_uint64,
            'pictureAccessGranularity': VkExtent2D,
            'minCodedExtent': VkExtent2D,
            'maxCodedExtent': VkExtent2D,
            'maxDpbSlots': ctypes.c_uint32,
            'maxActiveReferencePictures': ctypes.c_uint32,
            'stdHeaderVersion': VkExtensionProperties,
        }


from .VkExtensionProperties import VkExtensionProperties
from .VkExtent2D import VkExtent2D

VkVideoCapabilitiesKHR._fields_ = [
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
