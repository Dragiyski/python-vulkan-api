import ctypes

class VkDisplayEventInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('displayEvent', ctypes.c_int),
    ]

VkDisplayEventInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'displayEvent': ctypes.c_int,
}
