import ctypes

class VkPhysicalDeviceTimelineSemaphoreProperties(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxTimelineSemaphoreValueDifference', ctypes.c_uint64),
    ]

VkPhysicalDeviceTimelineSemaphoreProperties._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'maxTimelineSemaphoreValueDifference': ctypes.c_uint64,
}
