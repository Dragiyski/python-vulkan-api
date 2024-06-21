import ctypes

class CType(ctypes.Structure):
    pass


VkBaseOutStructure = CType
CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.POINTER(VkBaseOutStructure)),
]
del VkBaseOutStructure
