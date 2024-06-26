import ctypes

class VkPipelineLibraryCreateInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('libraryCount', ctypes.c_uint32),
        ('pLibraries', ctypes.POINTER(ctypes.c_void_p)),
    ]

    _init_ = []
    _extends_ = {
        'VkGraphicsPipelineCreateInfo',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkExecutionGraphPipelineCreateInfoAMDX',
        'VkRayTracingPipelineCreateInfoKHR',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'libraryCount': 'library_count',
        'pLibraries': 'libraries',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_pipeline_library',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PIPELINE_LIBRARY_CREATE_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_LIBRARY_CREATE_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkPipelineLibraryCreateInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'libraryCount': ctypes.c_uint32,
    'pLibraries': ctypes.POINTER(ctypes.c_void_p),
}
