import ctypes

class VkCopyImageToBufferInfo2(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkBufferImageCopy2',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkCmdCopyImageToBuffer2',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'srcImage': 'src_image',
        'srcImageLayout': 'src_image_layout',
        'dstBuffer': 'dst_buffer',
        'regionCount': 'region_count',
        'pRegions': 'regions',
    }
    _vk_versions_ = {
        (1, 3),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'srcImageLayout': 'VkImageLayout',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_COPY_IMAGE_TO_BUFFER_INFO_2'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_COPY_IMAGE_TO_BUFFER_INFO_2
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkBufferImageCopy2 import VkBufferImageCopy2

VkCopyImageToBufferInfo2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('srcImage', ctypes.c_void_p),
    ('srcImageLayout', ctypes.c_int),
    ('dstBuffer', ctypes.c_void_p),
    ('regionCount', ctypes.c_uint32),
    ('pRegions', ctypes.POINTER(VkBufferImageCopy2)),
]

VkCopyImageToBufferInfo2._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'srcImage': ctypes.c_void_p,
    'srcImageLayout': ctypes.c_int,
    'dstBuffer': ctypes.c_void_p,
    'regionCount': ctypes.c_uint32,
    'pRegions': ctypes.POINTER(VkBufferImageCopy2),
}
