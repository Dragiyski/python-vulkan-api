import ctypes

class CType(ctypes.Structure):
    pass

from .VkVideoPictureResourceInfoKHR import CType as VkVideoPictureResourceInfoKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('slotIndex', ctypes.c_int32),
    ('pPictureResource', ctypes.POINTER(VkVideoPictureResourceInfoKHR)),
]
