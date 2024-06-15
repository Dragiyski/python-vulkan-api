import ctypes, sys

class VkBufferMemoryRequirementsInfo2(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('buffer', ctypes.c_void_p),
    ]

sys.modules[__name__] = VkBufferMemoryRequirementsInfo2