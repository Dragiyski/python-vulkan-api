import ctypes

class VkPhysicalDeviceTimelineSemaphoreFeatures(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('timelineSemaphore', ctypes.c_uint32),
    ]

VkPhysicalDeviceTimelineSemaphoreFeatures._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'timelineSemaphore': ctypes.c_uint32,
}
