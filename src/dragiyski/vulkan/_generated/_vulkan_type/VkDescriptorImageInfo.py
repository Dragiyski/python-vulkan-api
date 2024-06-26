import ctypes

class VkDescriptorImageInfo(ctypes.Structure):
    _fields_ = [
        ('sampler', ctypes.c_void_p),
        ('imageView', ctypes.c_void_p),
        ('imageLayout', ctypes.c_int),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkDescriptorDataEXT',
        'VkWriteDescriptorSet',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sampler': 'sampler',
        'imageView': 'image_view',
        'imageLayout': 'image_layout',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'imageLayout': 'VkImageLayout',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkDescriptorImageInfo._type_ = {
    'sampler': ctypes.c_void_p,
    'imageView': ctypes.c_void_p,
    'imageLayout': ctypes.c_int,
}
