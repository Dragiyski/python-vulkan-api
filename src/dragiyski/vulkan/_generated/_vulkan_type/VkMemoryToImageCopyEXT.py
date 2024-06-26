import ctypes

class VkMemoryToImageCopyEXT(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkExtent3D',
        'VkImageSubresourceLayers',
        'VkOffset3D',
    }
    _included_in_ = {
        'VkCopyMemoryToImageInfoEXT',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'pHostPointer': 'host_pointer',
        'memoryRowLength': 'memory_row_length',
        'memoryImageHeight': 'memory_image_height',
        'imageSubresource': 'image_subresource',
        'imageOffset': 'image_offset',
        'imageExtent': 'image_extent',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_host_image_copy',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_MEMORY_TO_IMAGE_COPY_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_MEMORY_TO_IMAGE_COPY_EXT
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkExtent3D import VkExtent3D
from .VkImageSubresourceLayers import VkImageSubresourceLayers
from .VkOffset3D import VkOffset3D

VkMemoryToImageCopyEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pHostPointer', ctypes.c_void_p),
    ('memoryRowLength', ctypes.c_uint32),
    ('memoryImageHeight', ctypes.c_uint32),
    ('imageSubresource', VkImageSubresourceLayers),
    ('imageOffset', VkOffset3D),
    ('imageExtent', VkExtent3D),
]

VkMemoryToImageCopyEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pHostPointer': ctypes.c_void_p,
    'memoryRowLength': ctypes.c_uint32,
    'memoryImageHeight': ctypes.c_uint32,
    'imageSubresource': VkImageSubresourceLayers,
    'imageOffset': VkOffset3D,
    'imageExtent': VkExtent3D,
}
