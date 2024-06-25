import ctypes

class VkExternalMemoryAcquireUnmodifiedEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('acquireUnmodifiedMemory', ctypes.c_uint32),
    ]

VkExternalMemoryAcquireUnmodifiedEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'acquireUnmodifiedMemory': ctypes.c_uint32,
}
