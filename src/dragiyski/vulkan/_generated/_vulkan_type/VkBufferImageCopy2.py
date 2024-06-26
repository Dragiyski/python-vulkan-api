import ctypes

class VkBufferImageCopy2(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkCopyCommandTransformInfoQCOM',
    }
    _includes_ = {
        'VkExtent3D',
        'VkImageSubresourceLayers',
        'VkOffset3D',
    }
    _included_in_ = {
        'VkCopyBufferToImageInfo2',
        'VkCopyImageToBufferInfo2',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'bufferOffset': 'buffer_offset',
        'bufferRowLength': 'buffer_row_length',
        'bufferImageHeight': 'buffer_image_height',
        'imageSubresource': 'image_subresource',
        'imageOffset': 'image_offset',
        'imageExtent': 'image_extent',
    }
    _vk_versions_ = {
        (1, 3),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_BUFFER_IMAGE_COPY_2'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_BUFFER_IMAGE_COPY_2
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkExtent3D import VkExtent3D
from .VkImageSubresourceLayers import VkImageSubresourceLayers
from .VkOffset3D import VkOffset3D

VkBufferImageCopy2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('bufferOffset', ctypes.c_uint64),
    ('bufferRowLength', ctypes.c_uint32),
    ('bufferImageHeight', ctypes.c_uint32),
    ('imageSubresource', VkImageSubresourceLayers),
    ('imageOffset', VkOffset3D),
    ('imageExtent', VkExtent3D),
]

VkBufferImageCopy2._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'bufferOffset': ctypes.c_uint64,
    'bufferRowLength': ctypes.c_uint32,
    'bufferImageHeight': ctypes.c_uint32,
    'imageSubresource': VkImageSubresourceLayers,
    'imageOffset': VkOffset3D,
    'imageExtent': VkExtent3D,
}
