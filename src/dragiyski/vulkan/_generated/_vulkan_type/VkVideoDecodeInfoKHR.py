import ctypes, sys

class VkVideoDecodeInfoKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkVideoDecodeInfoKHR

from . import VkVideoPictureResourceInfoKHR
from . import VkVideoReferenceSlotInfoKHR

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
