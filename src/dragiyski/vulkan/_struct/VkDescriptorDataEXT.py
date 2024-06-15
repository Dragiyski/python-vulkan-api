import ctypes, sys

class VkDescriptorDataEXT(ctypes.Union):
    pass

sys.modules[__name__] = VkDescriptorDataEXT

from . import VkDescriptorImageInfo
from . import VkDescriptorAddressInfoEXT

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
