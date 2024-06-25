import ctypes

class VkCalibratedTimestampInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('timeDomain', ctypes.c_int),
    ]

VkCalibratedTimestampInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'timeDomain': ctypes.c_int,
}
