import ctypes

class VkConditionalRenderingBeginInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('buffer', ctypes.c_void_p),
        ('offset', ctypes.c_uint64),
        ('flags', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkCmdBeginConditionalRenderingEXT',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'buffer': 'buffer',
        'offset': 'offset',
        'flags': 'flags',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_conditional_rendering',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkConditionalRenderingFlagsEXT',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_CONDITIONAL_RENDERING_BEGIN_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_CONDITIONAL_RENDERING_BEGIN_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkConditionalRenderingBeginInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'buffer': ctypes.c_void_p,
    'offset': ctypes.c_uint64,
    'flags': ctypes.c_uint32,
}
