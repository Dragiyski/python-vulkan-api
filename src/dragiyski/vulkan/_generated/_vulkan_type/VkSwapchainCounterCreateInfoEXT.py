import ctypes

class VkSwapchainCounterCreateInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('surfaceCounters', ctypes.c_uint32),
    ]

VkSwapchainCounterCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'surfaceCounters': ctypes.c_uint32,
}
