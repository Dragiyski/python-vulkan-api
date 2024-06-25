import ctypes

class VkMemoryDedicatedRequirements(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('prefersDedicatedAllocation', ctypes.c_uint32),
        ('requiresDedicatedAllocation', ctypes.c_uint32),
    ]

VkMemoryDedicatedRequirements._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'prefersDedicatedAllocation': ctypes.c_uint32,
    'requiresDedicatedAllocation': ctypes.c_uint32,
}
