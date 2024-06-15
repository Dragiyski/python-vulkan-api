import ctypes, sys

class VkPhysicalDeviceFragmentDensityMap2PropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('subsampledLoads', ctypes.c_uint32),
        ('subsampledCoarseReconstructionEarlyAccess', ctypes.c_uint32),
        ('maxSubsampledArrayLayers', ctypes.c_uint32),
        ('maxDescriptorSetSubsampledSamplers', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceFragmentDensityMap2PropertiesEXT
