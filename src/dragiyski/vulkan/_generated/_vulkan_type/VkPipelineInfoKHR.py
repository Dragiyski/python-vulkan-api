import ctypes, sys

class VkPipelineInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pipeline', ctypes.c_void_p),
    ]

sys.modules[__name__] = VkPipelineInfoKHR
