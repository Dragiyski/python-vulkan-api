import ctypes, sys

class VkDeviceGroupCommandBufferBeginInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('deviceMask', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkDeviceGroupCommandBufferBeginInfo
