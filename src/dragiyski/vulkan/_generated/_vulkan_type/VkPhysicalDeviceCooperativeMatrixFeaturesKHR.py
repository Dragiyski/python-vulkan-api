import ctypes

class VkPhysicalDeviceCooperativeMatrixFeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('cooperativeMatrix', ctypes.c_uint32),
        ('cooperativeMatrixRobustBufferAccess', ctypes.c_uint32),
    ]

VkPhysicalDeviceCooperativeMatrixFeaturesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'cooperativeMatrix': ctypes.c_uint32,
    'cooperativeMatrixRobustBufferAccess': ctypes.c_uint32,
}
