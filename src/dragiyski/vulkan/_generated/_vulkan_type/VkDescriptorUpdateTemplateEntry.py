import ctypes

class VkDescriptorUpdateTemplateEntry(ctypes.Structure):
    _fields_ = [
        ('dstBinding', ctypes.c_uint32),
        ('dstArrayElement', ctypes.c_uint32),
        ('descriptorCount', ctypes.c_uint32),
        ('descriptorType', ctypes.c_int),
        ('offset', ctypes.c_size_t),
        ('stride', ctypes.c_size_t),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkDescriptorUpdateTemplateCreateInfo',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'dstBinding': 'dst_binding',
        'dstArrayElement': 'dst_array_element',
        'descriptorCount': 'descriptor_count',
        'descriptorType': 'descriptor_type',
        'offset': 'offset',
        'stride': 'stride',
    }
    _vk_versions_ = {
        (1, 1),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'descriptorType': 'VkDescriptorType',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkDescriptorUpdateTemplateEntry._type_ = {
    'dstBinding': ctypes.c_uint32,
    'dstArrayElement': ctypes.c_uint32,
    'descriptorCount': ctypes.c_uint32,
    'descriptorType': ctypes.c_int,
    'offset': ctypes.c_size_t,
    'stride': ctypes.c_size_t,
}
