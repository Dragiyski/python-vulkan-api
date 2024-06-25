import ctypes

class VkPhysicalDevicePageableDeviceLocalMemoryFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pageableDeviceLocalMemory', ctypes.c_uint32),
    ]

VkPhysicalDevicePageableDeviceLocalMemoryFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pageableDeviceLocalMemory': ctypes.c_uint32,
}
