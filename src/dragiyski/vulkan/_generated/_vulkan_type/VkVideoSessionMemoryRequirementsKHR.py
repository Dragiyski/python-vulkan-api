import ctypes

class VkVideoSessionMemoryRequirementsKHR(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkMemoryRequirements',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = {
        'vkGetVideoSessionMemoryRequirementsKHR',
    }
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'memoryBindIndex': 'memory_bind_index',
        'memoryRequirements': 'memory_requirements',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_video_queue',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VIDEO_SESSION_MEMORY_REQUIREMENTS_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_SESSION_MEMORY_REQUIREMENTS_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkMemoryRequirements import VkMemoryRequirements

VkVideoSessionMemoryRequirementsKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('memoryBindIndex', ctypes.c_uint32),
    ('memoryRequirements', VkMemoryRequirements),
]

VkVideoSessionMemoryRequirementsKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'memoryBindIndex': ctypes.c_uint32,
    'memoryRequirements': VkMemoryRequirements,
}
