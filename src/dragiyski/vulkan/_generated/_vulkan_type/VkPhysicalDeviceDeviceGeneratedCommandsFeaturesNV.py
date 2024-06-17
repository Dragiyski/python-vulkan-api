import ctypes, sys

class VkPhysicalDeviceDeviceGeneratedCommandsFeaturesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('deviceGeneratedCommands', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceDeviceGeneratedCommandsFeaturesNV
