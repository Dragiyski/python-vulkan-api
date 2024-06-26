import ctypes

class VkOffset3D(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int32),
        ('y', ctypes.c_int32),
        ('z', ctypes.c_int32),
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
        'VkSparseImageMemoryBind',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'x': 'x',
        'y': 'y',
        'z': 'z',
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

VkOffset3D._type_ = {
    'x': ctypes.c_int32,
    'y': ctypes.c_int32,
    'z': ctypes.c_int32,
}
