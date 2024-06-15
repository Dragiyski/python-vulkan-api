import ctypes, sys

class VkPushDescriptorSetInfoKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkPushDescriptorSetInfoKHR

from . import VkWriteDescriptorSet

VkPushDescriptorSetInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('stageFlags', ctypes.c_uint32),
    ('layout', ctypes.c_void_p),
    ('set', ctypes.c_uint32),
    ('descriptorWriteCount', ctypes.c_uint32),
    ('pDescriptorWrites', ctypes.POINTER(VkWriteDescriptorSet)),
]
