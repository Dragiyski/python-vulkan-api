import ctypes

class VkCopyMemoryToImageIndirectCommandNV(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkExtent3D',
        'VkImageSubresourceLayers',
        'VkOffset3D',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'srcAddress': 'src_address',
        'bufferRowLength': 'buffer_row_length',
        'bufferImageHeight': 'buffer_image_height',
        'imageSubresource': 'image_subresource',
        'imageOffset': 'image_offset',
        'imageExtent': 'image_extent',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_copy_memory_indirect',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkExtent3D import VkExtent3D
from .VkImageSubresourceLayers import VkImageSubresourceLayers
from .VkOffset3D import VkOffset3D

VkCopyMemoryToImageIndirectCommandNV._fields_ = [
    ('srcAddress', ctypes.c_uint64),
    ('bufferRowLength', ctypes.c_uint32),
    ('bufferImageHeight', ctypes.c_uint32),
    ('imageSubresource', VkImageSubresourceLayers),
    ('imageOffset', VkOffset3D),
    ('imageExtent', VkExtent3D),
]

VkCopyMemoryToImageIndirectCommandNV._type_ = {
    'srcAddress': ctypes.c_uint64,
    'bufferRowLength': ctypes.c_uint32,
    'bufferImageHeight': ctypes.c_uint32,
    'imageSubresource': VkImageSubresourceLayers,
    'imageOffset': VkOffset3D,
    'imageExtent': VkExtent3D,
}
