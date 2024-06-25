import ctypes

class VkPhysicalDeviceCudaKernelLaunchPropertiesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('computeCapabilityMinor', ctypes.c_uint32),
        ('computeCapabilityMajor', ctypes.c_uint32),
    ]

VkPhysicalDeviceCudaKernelLaunchPropertiesNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'computeCapabilityMinor': ctypes.c_uint32,
    'computeCapabilityMajor': ctypes.c_uint32,
}
