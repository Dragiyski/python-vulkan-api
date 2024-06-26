import ctypes

class VkImageSubresourceLayers(ctypes.Structure):
    _fields_ = [
        ('aspectMask', ctypes.c_uint32),
        ('mipLevel', ctypes.c_uint32),
        ('baseArrayLayer', ctypes.c_uint32),
        ('layerCount', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkBufferImageCopy',
        'VkBufferImageCopy2',
        'VkCopyMemoryToImageIndirectCommandNV',
        'VkImageBlit',
        'VkImageBlit2',
        'VkImageCopy',
        'VkImageCopy2',
        'VkImageResolve',
        'VkImageResolve2',
        'VkImageToMemoryCopyEXT',
        'VkMemoryToImageCopyEXT',
    }
    _input_of_ = {
        'vkCmdCopyMemoryToImageIndirectNV',
    }
    _output_of_ = set()
    _python_name_ = {
        'aspectMask': 'aspect_mask',
        'mipLevel': 'mip_level',
        'baseArrayLayer': 'base_array_layer',
        'layerCount': 'layer_count',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'aspectMask': 'VkImageAspectFlags',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkImageSubresourceLayers._type_ = {
    'aspectMask': ctypes.c_uint32,
    'mipLevel': ctypes.c_uint32,
    'baseArrayLayer': ctypes.c_uint32,
    'layerCount': ctypes.c_uint32,
}
