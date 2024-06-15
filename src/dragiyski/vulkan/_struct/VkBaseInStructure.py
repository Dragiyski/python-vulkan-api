import ctypes, sys

class VkBaseInStructure(ctypes.Structure):
    pass

sys.modules[__name__] = VkBaseInStructure


VkBaseInStructure._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.POINTER(VkBaseInStructure)),
]
