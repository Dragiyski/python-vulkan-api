import ctypes

class VkDescriptorDataEXT(ctypes.Union):
    pass

from .VkDescriptorAddressInfoEXT import VkDescriptorAddressInfoEXT
from .VkDescriptorImageInfo import VkDescriptorImageInfo

VkDescriptorDataEXT._fields_ = [
    ('pSampler', ctypes.POINTER(ctypes.c_void_p)),
    ('pCombinedImageSampler', ctypes.POINTER(VkDescriptorImageInfo)),
    ('pInputAttachmentImage', ctypes.POINTER(VkDescriptorImageInfo)),
    ('pSampledImage', ctypes.POINTER(VkDescriptorImageInfo)),
    ('pStorageImage', ctypes.POINTER(VkDescriptorImageInfo)),
    ('pUniformTexelBuffer', ctypes.POINTER(VkDescriptorAddressInfoEXT)),
    ('pStorageTexelBuffer', ctypes.POINTER(VkDescriptorAddressInfoEXT)),
    ('pUniformBuffer', ctypes.POINTER(VkDescriptorAddressInfoEXT)),
    ('pStorageBuffer', ctypes.POINTER(VkDescriptorAddressInfoEXT)),
    ('accelerationStructure', ctypes.c_uint64),
]

VkDescriptorDataEXT._type_ = {
    'pSampler': ctypes.POINTER(ctypes.c_void_p),
    'pCombinedImageSampler': ctypes.POINTER(VkDescriptorImageInfo),
    'pInputAttachmentImage': ctypes.POINTER(VkDescriptorImageInfo),
    'pSampledImage': ctypes.POINTER(VkDescriptorImageInfo),
    'pStorageImage': ctypes.POINTER(VkDescriptorImageInfo),
    'pUniformTexelBuffer': ctypes.POINTER(VkDescriptorAddressInfoEXT),
    'pStorageTexelBuffer': ctypes.POINTER(VkDescriptorAddressInfoEXT),
    'pUniformBuffer': ctypes.POINTER(VkDescriptorAddressInfoEXT),
    'pStorageBuffer': ctypes.POINTER(VkDescriptorAddressInfoEXT),
    'accelerationStructure': ctypes.c_uint64,
}
