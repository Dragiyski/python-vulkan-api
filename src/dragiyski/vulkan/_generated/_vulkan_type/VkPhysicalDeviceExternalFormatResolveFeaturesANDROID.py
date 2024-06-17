import ctypes, sys

class VkPhysicalDeviceExternalFormatResolveFeaturesANDROID(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('externalFormatResolve', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceExternalFormatResolveFeaturesANDROID
