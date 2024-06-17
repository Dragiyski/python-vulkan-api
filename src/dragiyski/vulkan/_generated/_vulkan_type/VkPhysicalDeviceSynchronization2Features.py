import ctypes, sys

class VkPhysicalDeviceSynchronization2Features(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('synchronization2', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceSynchronization2Features
