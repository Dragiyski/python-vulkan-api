import ctypes

class VkDeviceBufferMemoryRequirements(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkBufferCreateInfo',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkGetDeviceBufferMemoryRequirements',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'pCreateInfo': 'create_info',
    }
    _vk_versions_ = {
        (1, 3),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_DEVICE_BUFFER_MEMORY_REQUIREMENTS'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_BUFFER_MEMORY_REQUIREMENTS
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkBufferCreateInfo import VkBufferCreateInfo

VkDeviceBufferMemoryRequirements._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pCreateInfo', ctypes.POINTER(VkBufferCreateInfo)),
]

VkDeviceBufferMemoryRequirements._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pCreateInfo': ctypes.POINTER(VkBufferCreateInfo),
}
