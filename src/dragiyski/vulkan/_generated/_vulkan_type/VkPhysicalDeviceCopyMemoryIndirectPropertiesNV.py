import ctypes

class VkPhysicalDeviceCopyMemoryIndirectPropertiesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('supportedQueues', ctypes.c_uint32),
    ]

VkPhysicalDeviceCopyMemoryIndirectPropertiesNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'supportedQueues': ctypes.c_uint32,
}
