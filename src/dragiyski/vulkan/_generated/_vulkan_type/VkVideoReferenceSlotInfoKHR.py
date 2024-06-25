import ctypes

class VkVideoReferenceSlotInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'slotIndex': ctypes.c_int32,
            'pPictureResource': ctypes.POINTER(VkVideoPictureResourceInfoKHR),
        }


from .VkVideoPictureResourceInfoKHR import VkVideoPictureResourceInfoKHR

VkVideoReferenceSlotInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('slotIndex', ctypes.c_int32),
    ('pPictureResource', ctypes.POINTER(VkVideoPictureResourceInfoKHR)),
]
