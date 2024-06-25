import ctypes

class VkDeviceEventInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('deviceEvent', ctypes.c_int),
    ]

VkDeviceEventInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'deviceEvent': ctypes.c_int,
}
