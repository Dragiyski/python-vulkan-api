import ctypes

class VkCopyMemoryToImageInfoEXT(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkMemoryToImageCopyEXT',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkCopyMemoryToImageEXT',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'dstImage': 'dst_image',
        'dstImageLayout': 'dst_image_layout',
        'regionCount': 'region_count',
        'pRegions': 'regions',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_host_image_copy',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkHostImageCopyFlagsEXT',
        'dstImageLayout': 'VkImageLayout',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_COPY_MEMORY_TO_IMAGE_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_COPY_MEMORY_TO_IMAGE_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkMemoryToImageCopyEXT import VkMemoryToImageCopyEXT

VkCopyMemoryToImageInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('dstImage', ctypes.c_void_p),
    ('dstImageLayout', ctypes.c_int),
    ('regionCount', ctypes.c_uint32),
    ('pRegions', ctypes.POINTER(VkMemoryToImageCopyEXT)),
]

VkCopyMemoryToImageInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'dstImage': ctypes.c_void_p,
    'dstImageLayout': ctypes.c_int,
    'regionCount': ctypes.c_uint32,
    'pRegions': ctypes.POINTER(VkMemoryToImageCopyEXT),
}
