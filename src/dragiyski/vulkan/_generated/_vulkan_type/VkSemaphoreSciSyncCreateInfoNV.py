import ctypes

class VkSemaphoreSciSyncCreateInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('semaphorePool', ctypes.c_void_p),
        ('pFence', ctypes.POINTER(ctypes.ARRAY(ctypes.c_uint64, 6))),
    ]

VkSemaphoreSciSyncCreateInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'semaphorePool': ctypes.c_void_p,
    'pFence': ctypes.POINTER(ctypes.ARRAY(ctypes.c_uint64, 6)),
}
