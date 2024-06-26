import ctypes

class VkDisplayPresentInfoKHR(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkPresentInfoKHR',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkRect2D',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'srcRect': 'src_rect',
        'dstRect': 'dst_rect',
        'persistent': 'persistent',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_display_swapchain',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_DISPLAY_PRESENT_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_DISPLAY_PRESENT_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkRect2D import VkRect2D

VkDisplayPresentInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('srcRect', VkRect2D),
    ('dstRect', VkRect2D),
    ('persistent', ctypes.c_uint32),
]

VkDisplayPresentInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'srcRect': VkRect2D,
    'dstRect': VkRect2D,
    'persistent': ctypes.c_uint32,
}
