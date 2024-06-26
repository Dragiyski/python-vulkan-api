import ctypes

class VkSubpassEndInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkSubpassFragmentDensityMapOffsetEndInfoQCOM',
    }
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkCmdEndRenderPass2',
        'vkCmdNextSubpass2',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
    }
    _vk_versions_ = {
        (1, 2),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_SUBPASS_END_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_SUBPASS_END_INFO
        for function in self._init_:
            function(self, *args, **kwargs)

VkSubpassEndInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
}
