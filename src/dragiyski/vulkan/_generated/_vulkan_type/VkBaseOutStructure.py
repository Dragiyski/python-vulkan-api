import ctypes, sys

class VkBaseOutStructure(ctypes.Structure):
    pass

sys.modules[__name__] = VkBaseOutStructure


VkBaseOutStructure._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.POINTER(VkBaseOutStructure)),
]
