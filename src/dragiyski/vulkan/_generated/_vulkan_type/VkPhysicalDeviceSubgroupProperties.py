import ctypes

class VkPhysicalDeviceSubgroupProperties(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('subgroupSize', ctypes.c_uint32),
        ('supportedStages', ctypes.c_uint32),
        ('supportedOperations', ctypes.c_uint32),
        ('quadOperationsInAllStages', ctypes.c_uint32),
    ]

VkPhysicalDeviceSubgroupProperties._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'subgroupSize': ctypes.c_uint32,
    'supportedStages': ctypes.c_uint32,
    'supportedOperations': ctypes.c_uint32,
    'quadOperationsInAllStages': ctypes.c_uint32,
}
