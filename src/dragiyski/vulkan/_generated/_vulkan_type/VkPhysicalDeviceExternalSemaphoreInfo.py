import ctypes

class VkPhysicalDeviceExternalSemaphoreInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('handleType', ctypes.c_uint32),
    ]

VkPhysicalDeviceExternalSemaphoreInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'handleType': ctypes.c_uint32,
}
