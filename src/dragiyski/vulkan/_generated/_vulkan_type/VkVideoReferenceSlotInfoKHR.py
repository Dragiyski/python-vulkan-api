import ctypes, sys

class VkVideoReferenceSlotInfoKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkVideoReferenceSlotInfoKHR

from . import VkVideoPictureResourceInfoKHR

VkVideoReferenceSlotInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('slotIndex', ctypes.c_int32),
    ('pPictureResource', ctypes.POINTER(VkVideoPictureResourceInfoKHR)),
]
