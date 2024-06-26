import ctypes

class VkPipelineSampleLocationsStateCreateInfoEXT(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkPipelineMultisampleStateCreateInfo',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkSampleLocationsInfoEXT',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'sampleLocationsEnable': 'sample_locations_enable',
        'sampleLocationsInfo': 'sample_locations_info',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_sample_locations',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PIPELINE_SAMPLE_LOCATIONS_STATE_CREATE_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_SAMPLE_LOCATIONS_STATE_CREATE_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkSampleLocationsInfoEXT import VkSampleLocationsInfoEXT

VkPipelineSampleLocationsStateCreateInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('sampleLocationsEnable', ctypes.c_uint32),
    ('sampleLocationsInfo', VkSampleLocationsInfoEXT),
]

VkPipelineSampleLocationsStateCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'sampleLocationsEnable': ctypes.c_uint32,
    'sampleLocationsInfo': VkSampleLocationsInfoEXT,
}
