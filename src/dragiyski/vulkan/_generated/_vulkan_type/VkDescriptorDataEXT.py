import ctypes

class VkDescriptorDataEXT(ctypes.Union):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkDescriptorAddressInfoEXT',
        'VkDescriptorImageInfo',
    }
    _included_in_ = {
        'VkDescriptorGetInfoEXT',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'pSampler': 'sampler',
        'pCombinedImageSampler': 'combined_image_sampler',
        'pInputAttachmentImage': 'input_attachment_image',
        'pSampledImage': 'sampled_image',
        'pStorageImage': 'storage_image',
        'pUniformTexelBuffer': 'uniform_texel_buffer',
        'pStorageTexelBuffer': 'storage_texel_buffer',
        'pUniformBuffer': 'uniform_buffer',
        'pStorageBuffer': 'storage_buffer',
        'accelerationStructure': 'acceleration_structure',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_descriptor_buffer',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


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
