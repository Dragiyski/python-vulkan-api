import ctypes

class VkPipelineExecutablePropertiesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('stages', ctypes.c_uint32),
        ('name', ctypes.ARRAY(ctypes.c_char, 256)),
        ('description', ctypes.ARRAY(ctypes.c_char, 256)),
        ('subgroupSize', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = {
        'vkGetPipelineExecutablePropertiesKHR',
    }
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'stages': 'stages',
        'name': 'name',
        'description': 'description',
        'subgroupSize': 'subgroup_size',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_pipeline_executable_properties',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'stages': 'VkShaderStageFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PIPELINE_EXECUTABLE_PROPERTIES_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_EXECUTABLE_PROPERTIES_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkPipelineExecutablePropertiesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'stages': ctypes.c_uint32,
    'name': ctypes.ARRAY(ctypes.c_char, 256),
    'description': ctypes.ARRAY(ctypes.c_char, 256),
    'subgroupSize': ctypes.c_uint32,
}
