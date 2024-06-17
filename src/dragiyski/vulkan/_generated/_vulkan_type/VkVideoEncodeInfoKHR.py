import ctypes, sys

class VkVideoEncodeInfoKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkVideoEncodeInfoKHR

from . import VkVideoPictureResourceInfoKHR
from . import VkVideoReferenceSlotInfoKHR

VkVideoEncodeInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('dstBuffer', ctypes.c_void_p),
    ('dstBufferOffset', ctypes.c_uint64),
    ('dstBufferRange', ctypes.c_uint64),
    ('srcPictureResource', VkVideoPictureResourceInfoKHR),
    ('pSetupReferenceSlot', ctypes.POINTER(VkVideoReferenceSlotInfoKHR)),
    ('referenceSlotCount', ctypes.c_uint32),
    ('pReferenceSlots', ctypes.POINTER(VkVideoReferenceSlotInfoKHR)),
    ('precedingExternallyEncodedBytes', ctypes.c_uint32),
]
