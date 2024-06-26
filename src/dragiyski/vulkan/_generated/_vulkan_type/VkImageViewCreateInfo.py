import ctypes

class VkImageViewCreateInfo(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkExportMetalObjectCreateInfoEXT',
        'VkImageViewASTCDecodeModeEXT',
        'VkImageViewMinLodCreateInfoEXT',
        'VkImageViewSampleWeightCreateInfoQCOM',
        'VkImageViewSlicedCreateInfoEXT',
        'VkImageViewUsageCreateInfo',
        'VkOpaqueCaptureDescriptorDataCreateInfoEXT',
        'VkSamplerYcbcrConversionInfo',
    }
    _includes_ = {
        'VkComponentMapping',
        'VkImageSubresourceRange',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkCreateImageView',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'image': 'image',
        'viewType': 'view_type',
        'format': 'format',
        'components': 'components',
        'subresourceRange': 'subresource_range',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkImageViewCreateFlags',
        'viewType': 'VkImageViewType',
        'format': 'VkFormat',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_IMAGE_VIEW_CREATE_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_VIEW_CREATE_INFO
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkComponentMapping import VkComponentMapping
from .VkImageSubresourceRange import VkImageSubresourceRange

VkImageViewCreateInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('image', ctypes.c_void_p),
    ('viewType', ctypes.c_int),
    ('format', ctypes.c_int),
    ('components', VkComponentMapping),
    ('subresourceRange', VkImageSubresourceRange),
]

VkImageViewCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'image': ctypes.c_void_p,
    'viewType': ctypes.c_int,
    'format': ctypes.c_int,
    'components': VkComponentMapping,
    'subresourceRange': VkImageSubresourceRange,
}
