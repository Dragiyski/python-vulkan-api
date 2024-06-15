import ctypes, sys

class VkPipelineCreateFlags2CreateInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint64),
    ]

sys.modules[__name__] = VkPipelineCreateFlags2CreateInfoKHR
