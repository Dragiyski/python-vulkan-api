import ctypes

class VkPhysicalDeviceNonSeamlessCubeMapFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('nonSeamlessCubeMap', ctypes.c_uint32),
    ]

VkPhysicalDeviceNonSeamlessCubeMapFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'nonSeamlessCubeMap': ctypes.c_uint32,
}
