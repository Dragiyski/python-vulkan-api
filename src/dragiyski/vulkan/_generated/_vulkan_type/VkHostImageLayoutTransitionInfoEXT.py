import ctypes

class VkHostImageLayoutTransitionInfoEXT(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkImageSubresourceRange',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkTransitionImageLayoutEXT',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'image': 'image',
        'oldLayout': 'old_layout',
        'newLayout': 'new_layout',
        'subresourceRange': 'subresource_range',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_host_image_copy',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'oldLayout': 'VkImageLayout',
        'newLayout': 'VkImageLayout',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_HOST_IMAGE_LAYOUT_TRANSITION_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_HOST_IMAGE_LAYOUT_TRANSITION_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkImageSubresourceRange import VkImageSubresourceRange

VkHostImageLayoutTransitionInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('image', ctypes.c_void_p),
    ('oldLayout', ctypes.c_int),
    ('newLayout', ctypes.c_int),
    ('subresourceRange', VkImageSubresourceRange),
]

VkHostImageLayoutTransitionInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'image': ctypes.c_void_p,
    'oldLayout': ctypes.c_int,
    'newLayout': ctypes.c_int,
    'subresourceRange': VkImageSubresourceRange,
}
