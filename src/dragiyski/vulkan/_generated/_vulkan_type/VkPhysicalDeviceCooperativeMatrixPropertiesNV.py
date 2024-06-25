import ctypes

class VkPhysicalDeviceCooperativeMatrixPropertiesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('cooperativeMatrixSupportedStages', ctypes.c_uint32),
    ]

VkPhysicalDeviceCooperativeMatrixPropertiesNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'cooperativeMatrixSupportedStages': ctypes.c_uint32,
}
