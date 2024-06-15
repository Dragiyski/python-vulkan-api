import ctypes, sys

class VkPhysicalDeviceMapMemoryPlacedPropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('minPlacedMemoryMapAlignment', ctypes.c_uint64),
    ]

sys.modules[__name__] = VkPhysicalDeviceMapMemoryPlacedPropertiesEXT
