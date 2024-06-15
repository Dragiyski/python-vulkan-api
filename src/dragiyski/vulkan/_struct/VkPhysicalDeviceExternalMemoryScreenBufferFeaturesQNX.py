import ctypes, sys

class VkPhysicalDeviceExternalMemoryScreenBufferFeaturesQNX(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('screenBufferImport', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceExternalMemoryScreenBufferFeaturesQNX
