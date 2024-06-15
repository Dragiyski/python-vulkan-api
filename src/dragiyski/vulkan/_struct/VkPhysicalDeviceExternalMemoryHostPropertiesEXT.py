import ctypes, sys

class VkPhysicalDeviceExternalMemoryHostPropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('minImportedHostPointerAlignment', ctypes.c_uint64),
    ]

sys.modules[__name__] = VkPhysicalDeviceExternalMemoryHostPropertiesEXT
