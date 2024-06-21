import ctypes

class CType(ctypes.Structure):
    pass


VkBaseInStructure = CType
CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.POINTER(VkBaseInStructure)),
]
del VkBaseInStructure
