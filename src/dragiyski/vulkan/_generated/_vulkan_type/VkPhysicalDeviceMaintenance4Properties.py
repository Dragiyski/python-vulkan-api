import ctypes, sys

class VkPhysicalDeviceMaintenance4Properties(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxBufferSize', ctypes.c_uint64),
    ]

sys.modules[__name__] = VkPhysicalDeviceMaintenance4Properties
