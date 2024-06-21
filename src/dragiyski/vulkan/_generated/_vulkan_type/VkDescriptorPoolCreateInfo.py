import ctypes

class CType(ctypes.Structure):
    pass

from .VkDescriptorPoolSize import CType as VkDescriptorPoolSize

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('maxSets', ctypes.c_uint32),
    ('poolSizeCount', ctypes.c_uint32),
    ('pPoolSizes', ctypes.POINTER(VkDescriptorPoolSize)),
]
