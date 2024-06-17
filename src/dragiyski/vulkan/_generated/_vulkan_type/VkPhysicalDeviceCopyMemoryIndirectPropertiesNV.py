import ctypes, sys

class VkPhysicalDeviceCopyMemoryIndirectPropertiesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('supportedQueues', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceCopyMemoryIndirectPropertiesNV
