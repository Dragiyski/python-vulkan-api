import ctypes

class VkPhysicalDeviceCudaKernelLaunchFeaturesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('cudaKernelLaunchFeatures', ctypes.c_uint32),
    ]

VkPhysicalDeviceCudaKernelLaunchFeaturesNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'cudaKernelLaunchFeatures': ctypes.c_uint32,
}
