import ctypes, sys

class VkVideoBeginCodingInfoKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkVideoBeginCodingInfoKHR

from . import VkVideoReferenceSlotInfoKHR

VkVideoBeginCodingInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('videoSession', ctypes.c_void_p),
    ('videoSessionParameters', ctypes.c_void_p),
    ('referenceSlotCount', ctypes.c_uint32),
    ('pReferenceSlots', ctypes.POINTER(VkVideoReferenceSlotInfoKHR)),
]
