import ctypes

class VkPhysicalDeviceMaintenance6FeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maintenance6', ctypes.c_uint32),
    ]

VkPhysicalDeviceMaintenance6FeaturesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'maintenance6': ctypes.c_uint32,
}
