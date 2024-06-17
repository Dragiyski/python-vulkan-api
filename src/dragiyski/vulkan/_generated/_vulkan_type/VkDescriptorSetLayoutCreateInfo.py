import ctypes, sys

class VkDescriptorSetLayoutCreateInfo(ctypes.Structure):
    pass

sys.modules[__name__] = VkDescriptorSetLayoutCreateInfo

from . import VkDescriptorSetLayoutBinding

VkDescriptorSetLayoutCreateInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('bindingCount', ctypes.c_uint32),
    ('pBindings', ctypes.POINTER(VkDescriptorSetLayoutBinding)),
]
