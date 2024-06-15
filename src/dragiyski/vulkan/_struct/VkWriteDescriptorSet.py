import ctypes, sys

class VkWriteDescriptorSet(ctypes.Structure):
    pass

sys.modules[__name__] = VkWriteDescriptorSet

from . import VkDescriptorImageInfo
from . import VkDescriptorBufferInfo

VkWriteDescriptorSet._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('dstSet', ctypes.c_void_p),
    ('dstBinding', ctypes.c_uint32),
    ('dstArrayElement', ctypes.c_uint32),
    ('descriptorCount', ctypes.c_uint32),
    ('descriptorType', ctypes.c_int),
    ('pImageInfo', ctypes.POINTER(VkDescriptorImageInfo)),
    ('pBufferInfo', ctypes.POINTER(VkDescriptorBufferInfo)),
    ('pTexelBufferView', ctypes.POINTER(ctypes.c_void_p)),
]
