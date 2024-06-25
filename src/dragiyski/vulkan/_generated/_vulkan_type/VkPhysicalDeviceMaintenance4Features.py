import ctypes

class VkPhysicalDeviceMaintenance4Features(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maintenance4', ctypes.c_uint32),
    ]

VkPhysicalDeviceMaintenance4Features._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'maintenance4': ctypes.c_uint32,
}
