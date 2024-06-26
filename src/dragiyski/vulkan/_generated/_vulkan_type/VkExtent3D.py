import ctypes

class VkExtent3D(ctypes.Structure):
    _fields_ = [
        ('width', ctypes.c_uint32),
        ('height', ctypes.c_uint32),
        ('depth', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkBufferImageCopy',
        'VkBufferImageCopy2',
        'VkCopyMemoryToImageIndirectCommandNV',
        'VkImageCopy',
        'VkImageCopy2',
        'VkImageCreateInfo',
        'VkImageFormatProperties',
        'VkImageResolve',
        'VkImageResolve2',
        'VkImageToMemoryCopyEXT',
        'VkMemoryToImageCopyEXT',
        'VkQueueFamilyProperties',
        'VkSparseImageFormatProperties',
        'VkSparseImageMemoryBind',
        'VkTilePropertiesQCOM',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'width': 'width',
        'height': 'height',
        'depth': 'depth',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkExtent3D._type_ = {
    'width': ctypes.c_uint32,
    'height': ctypes.c_uint32,
    'depth': ctypes.c_uint32,
}
