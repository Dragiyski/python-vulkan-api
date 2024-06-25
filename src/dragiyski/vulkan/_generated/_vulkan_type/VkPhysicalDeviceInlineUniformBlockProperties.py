import ctypes

class VkPhysicalDeviceInlineUniformBlockProperties(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'maxInlineUniformBlockSize': ctypes.c_uint32,
            'maxPerStageDescriptorInlineUniformBlocks': ctypes.c_uint32,
            'maxPerStageDescriptorUpdateAfterBindInlineUniformBlocks': ctypes.c_uint32,
            'maxDescriptorSetInlineUniformBlocks': ctypes.c_uint32,
            'maxDescriptorSetUpdateAfterBindInlineUniformBlocks': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxInlineUniformBlockSize', ctypes.c_uint32),
        ('maxPerStageDescriptorInlineUniformBlocks', ctypes.c_uint32),
        ('maxPerStageDescriptorUpdateAfterBindInlineUniformBlocks', ctypes.c_uint32),
        ('maxDescriptorSetInlineUniformBlocks', ctypes.c_uint32),
        ('maxDescriptorSetUpdateAfterBindInlineUniformBlocks', ctypes.c_uint32),
    ]
