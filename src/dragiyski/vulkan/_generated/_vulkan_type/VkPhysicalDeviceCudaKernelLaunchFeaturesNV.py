import ctypes, sys

class VkPhysicalDeviceCudaKernelLaunchFeaturesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('cudaKernelLaunchFeatures', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceCudaKernelLaunchFeaturesNV
