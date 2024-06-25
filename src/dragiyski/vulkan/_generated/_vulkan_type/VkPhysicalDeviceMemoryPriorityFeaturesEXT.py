import ctypes

class VkPhysicalDeviceMemoryPriorityFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('memoryPriority', ctypes.c_uint32),
    ]

VkPhysicalDeviceMemoryPriorityFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'memoryPriority': ctypes.c_uint32,
}
