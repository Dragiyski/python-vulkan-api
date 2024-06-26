import ctypes

class VkDescriptorSetBindingReferenceVALVE(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('descriptorSetLayout', ctypes.c_void_p),
        ('binding', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkGetDescriptorSetLayoutHostMappingInfoVALVE',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'descriptorSetLayout': 'descriptor_set_layout',
        'binding': 'binding',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_VALVE_descriptor_set_host_mapping',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_DESCRIPTOR_SET_BINDING_REFERENCE_VALVE'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_DESCRIPTOR_SET_BINDING_REFERENCE_VALVE
        for function in self._init_:
            function(self, *args, **kwargs)

VkDescriptorSetBindingReferenceVALVE._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'descriptorSetLayout': ctypes.c_void_p,
    'binding': ctypes.c_uint32,
}
