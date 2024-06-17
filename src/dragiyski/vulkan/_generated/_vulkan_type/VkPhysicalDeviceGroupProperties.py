import ctypes, sys

class VkPhysicalDeviceGroupProperties(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('physicalDeviceCount', ctypes.c_uint32),
        ('physicalDevices', ctypes.ARRAY(ctypes.c_void_p, 32)),
        ('subsetAllocation', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceGroupProperties
