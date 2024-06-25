import ctypes

class VkBaseOutStructure(ctypes.Structure):
    pass


VkBaseOutStructure._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.POINTER(VkBaseOutStructure)),
]

VkBaseOutStructure._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.POINTER(VkBaseOutStructure),
}
