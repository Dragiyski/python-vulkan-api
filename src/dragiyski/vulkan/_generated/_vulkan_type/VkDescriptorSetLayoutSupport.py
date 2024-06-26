import ctypes

class VkDescriptorSetLayoutSupport(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('supported', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkDescriptorSetVariableDescriptorCountLayoutSupport',
    }
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = {
        'vkGetDescriptorSetLayoutSupport',
    }
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'supported': 'supported',
    }
    _vk_versions_ = {
        (1, 1),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_DESCRIPTOR_SET_LAYOUT_SUPPORT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_DESCRIPTOR_SET_LAYOUT_SUPPORT
        for function in self._init_:
            function(self, *args, **kwargs)

VkDescriptorSetLayoutSupport._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'supported': ctypes.c_uint32,
}
