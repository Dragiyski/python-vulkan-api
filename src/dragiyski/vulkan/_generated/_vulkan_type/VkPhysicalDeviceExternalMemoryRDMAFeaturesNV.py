import ctypes

class VkPhysicalDeviceExternalMemoryRDMAFeaturesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('externalMemoryRDMA', ctypes.c_uint32),
    ]

VkPhysicalDeviceExternalMemoryRDMAFeaturesNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'externalMemoryRDMA': ctypes.c_uint32,
}
