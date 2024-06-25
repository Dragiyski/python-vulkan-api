import ctypes

class VkWriteDescriptorSet(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'dstSet': ctypes.c_void_p,
            'dstBinding': ctypes.c_uint32,
            'dstArrayElement': ctypes.c_uint32,
            'descriptorCount': ctypes.c_uint32,
            'descriptorType': ctypes.c_int,
            'pImageInfo': ctypes.POINTER(VkDescriptorImageInfo),
            'pBufferInfo': ctypes.POINTER(VkDescriptorBufferInfo),
            'pTexelBufferView': ctypes.POINTER(ctypes.c_void_p),
        }


from .VkDescriptorBufferInfo import VkDescriptorBufferInfo
from .VkDescriptorImageInfo import VkDescriptorImageInfo

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
