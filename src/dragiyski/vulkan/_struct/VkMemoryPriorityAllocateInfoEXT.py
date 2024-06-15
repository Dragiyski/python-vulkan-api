import ctypes, sys

class VkMemoryPriorityAllocateInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('priority', ctypes.c_float),
    ]

sys.modules[__name__] = VkMemoryPriorityAllocateInfoEXT
