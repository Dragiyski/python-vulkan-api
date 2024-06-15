import ctypes, sys

class VkDeviceGroupDeviceCreateInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('physicalDeviceCount', ctypes.c_uint32),
        ('pPhysicalDevices', ctypes.POINTER(ctypes.c_void_p)),
    ]

sys.modules[__name__] = VkDeviceGroupDeviceCreateInfo
