import ctypes

class VkBaseInStructure(ctypes.Structure):
    pass


VkBaseInStructure._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.POINTER(VkBaseInStructure)),
]

VkBaseInStructure._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.POINTER(VkBaseInStructure),
}
