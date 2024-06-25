import ctypes

class VkDeviceMemoryOverallocationCreateInfoAMD(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('overallocationBehavior', ctypes.c_int),
    ]

VkDeviceMemoryOverallocationCreateInfoAMD._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'overallocationBehavior': ctypes.c_int,
}
