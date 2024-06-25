import ctypes

class VkDeviceQueueInfo2(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('queueFamilyIndex', ctypes.c_uint32),
        ('queueIndex', ctypes.c_uint32),
    ]

VkDeviceQueueInfo2._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'queueFamilyIndex': ctypes.c_uint32,
    'queueIndex': ctypes.c_uint32,
}
