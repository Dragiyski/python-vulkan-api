import ctypes

class VkVideoBeginCodingInfoKHR(ctypes.Structure):
    pass

from .VkVideoReferenceSlotInfoKHR import VkVideoReferenceSlotInfoKHR

VkVideoBeginCodingInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('videoSession', ctypes.c_void_p),
    ('videoSessionParameters', ctypes.c_void_p),
    ('referenceSlotCount', ctypes.c_uint32),
    ('pReferenceSlots', ctypes.POINTER(VkVideoReferenceSlotInfoKHR)),
]

VkVideoBeginCodingInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'videoSession': ctypes.c_void_p,
    'videoSessionParameters': ctypes.c_void_p,
    'referenceSlotCount': ctypes.c_uint32,
    'pReferenceSlots': ctypes.POINTER(VkVideoReferenceSlotInfoKHR),
}
