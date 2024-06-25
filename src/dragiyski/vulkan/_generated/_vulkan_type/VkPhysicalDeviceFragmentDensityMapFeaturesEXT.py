import ctypes

class VkPhysicalDeviceFragmentDensityMapFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('fragmentDensityMap', ctypes.c_uint32),
        ('fragmentDensityMapDynamic', ctypes.c_uint32),
        ('fragmentDensityMapNonSubsampledImages', ctypes.c_uint32),
    ]

VkPhysicalDeviceFragmentDensityMapFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'fragmentDensityMap': ctypes.c_uint32,
    'fragmentDensityMapDynamic': ctypes.c_uint32,
    'fragmentDensityMapNonSubsampledImages': ctypes.c_uint32,
}
