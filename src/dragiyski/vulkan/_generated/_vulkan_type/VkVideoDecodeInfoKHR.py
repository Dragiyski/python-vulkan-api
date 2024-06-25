import ctypes

class VkVideoDecodeInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'flags': ctypes.c_uint32,
            'srcBuffer': ctypes.c_void_p,
            'srcBufferOffset': ctypes.c_uint64,
            'srcBufferRange': ctypes.c_uint64,
            'dstPictureResource': VkVideoPictureResourceInfoKHR,
            'pSetupReferenceSlot': ctypes.POINTER(VkVideoReferenceSlotInfoKHR),
            'referenceSlotCount': ctypes.c_uint32,
            'pReferenceSlots': ctypes.POINTER(VkVideoReferenceSlotInfoKHR),
        }


from .VkVideoPictureResourceInfoKHR import VkVideoPictureResourceInfoKHR
from .VkVideoReferenceSlotInfoKHR import VkVideoReferenceSlotInfoKHR

VkVideoDecodeInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('srcBuffer', ctypes.c_void_p),
    ('srcBufferOffset', ctypes.c_uint64),
    ('srcBufferRange', ctypes.c_uint64),
    ('dstPictureResource', VkVideoPictureResourceInfoKHR),
    ('pSetupReferenceSlot', ctypes.POINTER(VkVideoReferenceSlotInfoKHR)),
    ('referenceSlotCount', ctypes.c_uint32),
    ('pReferenceSlots', ctypes.POINTER(VkVideoReferenceSlotInfoKHR)),
]
