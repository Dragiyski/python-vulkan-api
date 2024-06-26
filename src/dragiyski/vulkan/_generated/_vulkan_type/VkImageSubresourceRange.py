import ctypes

class VkImageSubresourceRange(ctypes.Structure):
    _fields_ = [
        ('aspectMask', ctypes.c_uint32),
        ('baseMipLevel', ctypes.c_uint32),
        ('levelCount', ctypes.c_uint32),
        ('baseArrayLayer', ctypes.c_uint32),
        ('layerCount', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkHostImageLayoutTransitionInfoEXT',
        'VkImageMemoryBarrier',
        'VkImageMemoryBarrier2',
        'VkImageViewCreateInfo',
    }
    _input_of_ = {
        'vkCmdClearColorImage',
        'vkCmdClearDepthStencilImage',
    }
    _output_of_ = set()
    _python_name_ = {
        'aspectMask': 'aspect_mask',
        'baseMipLevel': 'base_mip_level',
        'levelCount': 'level_count',
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

VkImageSubresourceRange._type_ = {
    'aspectMask': ctypes.c_uint32,
    'baseMipLevel': ctypes.c_uint32,
    'levelCount': ctypes.c_uint32,
    'baseArrayLayer': ctypes.c_uint32,
    'layerCount': ctypes.c_uint32,
}
