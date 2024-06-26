import ctypes

class VkCopyImageToImageInfoEXT(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkImageCopy2',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkCopyImageToImageEXT',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'srcImage': 'src_image',
        'srcImageLayout': 'src_image_layout',
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
        'srcImageLayout': 'VkImageLayout',
        'dstImageLayout': 'VkImageLayout',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_COPY_IMAGE_TO_IMAGE_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_COPY_IMAGE_TO_IMAGE_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkImageCopy2 import VkImageCopy2

VkCopyImageToImageInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('srcImage', ctypes.c_void_p),
    ('srcImageLayout', ctypes.c_int),
    ('dstImage', ctypes.c_void_p),
    ('dstImageLayout', ctypes.c_int),
    ('regionCount', ctypes.c_uint32),
    ('pRegions', ctypes.POINTER(VkImageCopy2)),
]

VkCopyImageToImageInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'srcImage': ctypes.c_void_p,
    'srcImageLayout': ctypes.c_int,
    'dstImage': ctypes.c_void_p,
    'dstImageLayout': ctypes.c_int,
    'regionCount': ctypes.c_uint32,
    'pRegions': ctypes.POINTER(VkImageCopy2),
}
