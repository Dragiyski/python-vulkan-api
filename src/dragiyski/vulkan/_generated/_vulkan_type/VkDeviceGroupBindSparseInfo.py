import ctypes

class VkDeviceGroupBindSparseInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('resourceDeviceIndex', ctypes.c_uint32),
        ('memoryDeviceIndex', ctypes.c_uint32),
    ]

VkDeviceGroupBindSparseInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'resourceDeviceIndex': ctypes.c_uint32,
    'memoryDeviceIndex': ctypes.c_uint32,
}
