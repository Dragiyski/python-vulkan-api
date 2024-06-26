import ctypes

class VkMutableDescriptorTypeListEXT(ctypes.Structure):
    _fields_ = [
        ('descriptorTypeCount', ctypes.c_uint32),
        ('pDescriptorTypes', ctypes.POINTER(ctypes.c_int)),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkMutableDescriptorTypeCreateInfoEXT',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'descriptorTypeCount': 'descriptor_type_count',
        'pDescriptorTypes': 'descriptor_types',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_mutable_descriptor_type',
    }
    _vk_enum_ = {
        'pDescriptorTypes': 'VkDescriptorType',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkMutableDescriptorTypeListEXT._type_ = {
    'descriptorTypeCount': ctypes.c_uint32,
    'pDescriptorTypes': ctypes.POINTER(ctypes.c_int),
}
