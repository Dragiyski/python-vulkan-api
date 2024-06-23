import ctypes

class CType(ctypes.Union):
    pass

from .VkDescriptorAddressInfoEXT import CType as VkDescriptorAddressInfoEXT
from .VkDescriptorImageInfo import CType as VkDescriptorImageInfo

CType._fields_ = [
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

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkDescriptorAddressInfoEXT',
        'VkDescriptorImageInfo',
    },
    'included_in': {
        'VkDescriptorGetInfoEXT',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'pSampler': {'python_name': ['p', 'sampler']},
        'pCombinedImageSampler': {'python_name': ['p', 'combined', 'image', 'sampler'], 'type': 'VkDescriptorImageInfo'},
        'pInputAttachmentImage': {'python_name': ['p', 'input', 'attachment', 'image'], 'type': 'VkDescriptorImageInfo'},
        'pSampledImage': {'python_name': ['p', 'sampled', 'image'], 'type': 'VkDescriptorImageInfo'},
        'pStorageImage': {'python_name': ['p', 'storage', 'image'], 'type': 'VkDescriptorImageInfo'},
        'pUniformTexelBuffer': {'python_name': ['p', 'uniform', 'texel', 'buffer'], 'type': 'VkDescriptorAddressInfoEXT'},
        'pStorageTexelBuffer': {'python_name': ['p', 'storage', 'texel', 'buffer'], 'type': 'VkDescriptorAddressInfoEXT'},
        'pUniformBuffer': {'python_name': ['p', 'uniform', 'buffer'], 'type': 'VkDescriptorAddressInfoEXT'},
        'pStorageBuffer': {'python_name': ['p', 'storage', 'buffer'], 'type': 'VkDescriptorAddressInfoEXT'},
        'accelerationStructure': {'python_name': ['acceleration', 'structure']},
    }
}
