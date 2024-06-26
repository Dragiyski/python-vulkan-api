import ctypes

class VkSparseImageMemoryRequirements(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkSparseImageFormatProperties',
    }
    _included_in_ = {
        'VkSparseImageMemoryRequirements2',
    }
    _input_of_ = set()
    _output_of_ = {
        'vkGetImageSparseMemoryRequirements',
    }
    _python_name_ = {
        'formatProperties': 'format_properties',
        'imageMipTailFirstLod': 'image_mip_tail_first_lod',
        'imageMipTailSize': 'image_mip_tail_size',
        'imageMipTailOffset': 'image_mip_tail_offset',
        'imageMipTailStride': 'image_mip_tail_stride',
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


from .VkSparseImageFormatProperties import VkSparseImageFormatProperties

VkSparseImageMemoryRequirements._fields_ = [
    ('formatProperties', VkSparseImageFormatProperties),
    ('imageMipTailFirstLod', ctypes.c_uint32),
    ('imageMipTailSize', ctypes.c_uint64),
    ('imageMipTailOffset', ctypes.c_uint64),
    ('imageMipTailStride', ctypes.c_uint64),
]

VkSparseImageMemoryRequirements._type_ = {
    'formatProperties': VkSparseImageFormatProperties,
    'imageMipTailFirstLod': ctypes.c_uint32,
    'imageMipTailSize': ctypes.c_uint64,
    'imageMipTailOffset': ctypes.c_uint64,
    'imageMipTailStride': ctypes.c_uint64,
}
