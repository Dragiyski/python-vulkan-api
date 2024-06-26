import ctypes

class VkPipelineExecutableStatisticKHR(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkPipelineExecutableStatisticValueKHR',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = {
        'vkGetPipelineExecutableStatisticsKHR',
    }
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'name': 'name',
        'description': 'description',
        'format': 'format',
        'value': 'value',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_pipeline_executable_properties',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'format': 'VkPipelineExecutableStatisticFormatKHR',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PIPELINE_EXECUTABLE_STATISTIC_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_EXECUTABLE_STATISTIC_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkPipelineExecutableStatisticValueKHR import VkPipelineExecutableStatisticValueKHR

VkPipelineExecutableStatisticKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('name', ctypes.ARRAY(ctypes.c_char, 256)),
    ('description', ctypes.ARRAY(ctypes.c_char, 256)),
    ('format', ctypes.c_int),
    ('value', VkPipelineExecutableStatisticValueKHR),
]

VkPipelineExecutableStatisticKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'name': ctypes.ARRAY(ctypes.c_char, 256),
    'description': ctypes.ARRAY(ctypes.c_char, 256),
    'format': ctypes.c_int,
    'value': VkPipelineExecutableStatisticValueKHR,
}
