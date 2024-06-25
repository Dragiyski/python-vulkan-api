import ctypes

class VkOutOfBandQueueTypeInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('queueType', ctypes.c_int),
    ]

VkOutOfBandQueueTypeInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'queueType': ctypes.c_int,
}
