import ctypes, sys

class VkExternalMemoryAcquireUnmodifiedEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('acquireUnmodifiedMemory', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkExternalMemoryAcquireUnmodifiedEXT
