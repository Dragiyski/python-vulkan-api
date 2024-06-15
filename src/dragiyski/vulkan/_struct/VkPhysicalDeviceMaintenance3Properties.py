import ctypes, sys

class VkPhysicalDeviceMaintenance3Properties(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxPerSetDescriptors', ctypes.c_uint32),
        ('maxMemoryAllocationSize', ctypes.c_uint64),
    ]

sys.modules[__name__] = VkPhysicalDeviceMaintenance3Properties
