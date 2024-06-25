import ctypes

class VkPhysicalDeviceFragmentDensityMap2PropertiesEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'subsampledLoads': ctypes.c_uint32,
            'subsampledCoarseReconstructionEarlyAccess': ctypes.c_uint32,
            'maxSubsampledArrayLayers': ctypes.c_uint32,
            'maxDescriptorSetSubsampledSamplers': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('subsampledLoads', ctypes.c_uint32),
        ('subsampledCoarseReconstructionEarlyAccess', ctypes.c_uint32),
        ('maxSubsampledArrayLayers', ctypes.c_uint32),
        ('maxDescriptorSetSubsampledSamplers', ctypes.c_uint32),
    ]
