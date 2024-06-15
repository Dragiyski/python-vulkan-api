import ctypes, sys

class VkPhysicalDevicePCIBusInfoPropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pciDomain', ctypes.c_uint32),
        ('pciBus', ctypes.c_uint32),
        ('pciDevice', ctypes.c_uint32),
        ('pciFunction', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDevicePCIBusInfoPropertiesEXT
