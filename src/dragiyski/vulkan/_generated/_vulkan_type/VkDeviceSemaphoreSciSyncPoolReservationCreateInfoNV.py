import ctypes

class VkDeviceSemaphoreSciSyncPoolReservationCreateInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('semaphoreSciSyncPoolRequestCount', ctypes.c_uint32),
    ]

VkDeviceSemaphoreSciSyncPoolReservationCreateInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'semaphoreSciSyncPoolRequestCount': ctypes.c_uint32,
}
