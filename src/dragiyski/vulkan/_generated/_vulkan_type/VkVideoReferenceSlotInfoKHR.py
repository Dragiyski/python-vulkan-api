import ctypes

class VkVideoReferenceSlotInfoKHR(ctypes.Structure):
    pass

from .VkVideoPictureResourceInfoKHR import VkVideoPictureResourceInfoKHR

VkVideoReferenceSlotInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('slotIndex', ctypes.c_int32),
    ('pPictureResource', ctypes.POINTER(VkVideoPictureResourceInfoKHR)),
]

VkVideoReferenceSlotInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'slotIndex': ctypes.c_int32,
    'pPictureResource': ctypes.POINTER(VkVideoPictureResourceInfoKHR),
}
