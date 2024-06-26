import ctypes

class VkCommandBufferInheritanceConditionalRenderingInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('conditionalRenderingEnable', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkCommandBufferInheritanceInfo',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'conditionalRenderingEnable': 'conditional_rendering_enable',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_conditional_rendering',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_COMMAND_BUFFER_INHERITANCE_CONDITIONAL_RENDERING_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_COMMAND_BUFFER_INHERITANCE_CONDITIONAL_RENDERING_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkCommandBufferInheritanceConditionalRenderingInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'conditionalRenderingEnable': ctypes.c_uint32,
}
