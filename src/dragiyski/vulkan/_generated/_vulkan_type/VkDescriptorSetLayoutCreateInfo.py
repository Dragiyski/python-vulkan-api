import ctypes

class CType(ctypes.Structure):
    pass

from .VkDescriptorSetLayoutBinding import CType as VkDescriptorSetLayoutBinding

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('bindingCount', ctypes.c_uint32),
    ('pBindings', ctypes.POINTER(VkDescriptorSetLayoutBinding)),
]
