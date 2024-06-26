import ctypes

class VkDescriptorSetVariableDescriptorCountLayoutSupport(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxVariableDescriptorCount', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkDescriptorSetLayoutSupport',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'maxVariableDescriptorCount': 'max_variable_descriptor_count',
    }
    _vk_versions_ = {
        (1, 2),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_DESCRIPTOR_SET_VARIABLE_DESCRIPTOR_COUNT_LAYOUT_SUPPORT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_DESCRIPTOR_SET_VARIABLE_DESCRIPTOR_COUNT_LAYOUT_SUPPORT
        for function in self._init_:
            function(self, *args, **kwargs)

VkDescriptorSetVariableDescriptorCountLayoutSupport._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'maxVariableDescriptorCount': ctypes.c_uint32,
}
