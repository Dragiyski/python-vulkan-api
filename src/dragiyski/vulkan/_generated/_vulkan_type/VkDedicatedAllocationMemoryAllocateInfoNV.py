import ctypes, sys

class VkDedicatedAllocationMemoryAllocateInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('image', ctypes.c_void_p),
        ('buffer', ctypes.c_void_p),
    ]

sys.modules[__name__] = VkDedicatedAllocationMemoryAllocateInfoNV
