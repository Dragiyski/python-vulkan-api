import ctypes

class VkPhysicalDeviceMaintenance5FeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maintenance5', ctypes.c_uint32),
    ]

VkPhysicalDeviceMaintenance5FeaturesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'maintenance5': ctypes.c_uint32,
}
