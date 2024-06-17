import ctypes, sys

class VkDeviceGroupPresentCapabilitiesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('presentMask', ctypes.ARRAY(ctypes.c_uint32, 32)),
        ('modes', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkDeviceGroupPresentCapabilitiesKHR
