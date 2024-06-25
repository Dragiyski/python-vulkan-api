import ctypes

class VkMemoryPriorityAllocateInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('priority', ctypes.c_float),
    ]

VkMemoryPriorityAllocateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'priority': ctypes.c_float,
}
