import ctypes, sys

class VkDescriptorPoolCreateInfo(ctypes.Structure):
    pass

sys.modules[__name__] = VkDescriptorPoolCreateInfo

from . import VkDescriptorPoolSize

VkDescriptorPoolCreateInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('maxSets', ctypes.c_uint32),
    ('poolSizeCount', ctypes.c_uint32),
    ('pPoolSizes', ctypes.POINTER(VkDescriptorPoolSize)),
]
