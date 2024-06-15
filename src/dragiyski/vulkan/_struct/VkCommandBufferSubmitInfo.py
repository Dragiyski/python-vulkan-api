import ctypes, sys

class VkCommandBufferSubmitInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('commandBuffer', ctypes.c_void_p),
        ('deviceMask', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkCommandBufferSubmitInfo
