import ctypes, sys

class VkDedicatedAllocationBufferCreateInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('dedicatedAllocation', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkDedicatedAllocationBufferCreateInfoNV
