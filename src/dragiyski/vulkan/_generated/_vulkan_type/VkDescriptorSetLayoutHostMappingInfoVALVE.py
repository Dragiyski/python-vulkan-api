import ctypes

class VkDescriptorSetLayoutHostMappingInfoVALVE(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('descriptorOffset', ctypes.c_size_t),
        ('descriptorSize', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = {
        'vkGetDescriptorSetLayoutHostMappingInfoVALVE',
    }
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'descriptorOffset': 'descriptor_offset',
        'descriptorSize': 'descriptor_size',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_VALVE_descriptor_set_host_mapping',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_DESCRIPTOR_SET_LAYOUT_HOST_MAPPING_INFO_VALVE'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_DESCRIPTOR_SET_LAYOUT_HOST_MAPPING_INFO_VALVE
        for function in self._init_:
            function(self, *args, **kwargs)

VkDescriptorSetLayoutHostMappingInfoVALVE._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'descriptorOffset': ctypes.c_size_t,
    'descriptorSize': ctypes.c_uint32,
}
