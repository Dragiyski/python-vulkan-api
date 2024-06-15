import ctypes, sys

class VkDeviceGroupPresentInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('swapchainCount', ctypes.c_uint32),
        ('pDeviceMasks', ctypes.POINTER(ctypes.c_uint32)),
        ('mode', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkDeviceGroupPresentInfoKHR
