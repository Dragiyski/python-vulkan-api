import ctypes

class VkPhysicalDeviceMemoryDecompressionFeaturesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('memoryDecompression', ctypes.c_uint32),
    ]

VkPhysicalDeviceMemoryDecompressionFeaturesNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'memoryDecompression': ctypes.c_uint32,
}
