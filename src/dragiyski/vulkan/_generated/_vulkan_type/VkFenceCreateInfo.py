import ctypes

class VkFenceCreateInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkExportFenceCreateInfo',
        'VkExportFenceWin32HandleInfoKHR',
    }
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkCreateFence',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkFenceCreateFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_FENCE_CREATE_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_FENCE_CREATE_INFO
        for function in self._init_:
            function(self, *args, **kwargs)

VkFenceCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
}
