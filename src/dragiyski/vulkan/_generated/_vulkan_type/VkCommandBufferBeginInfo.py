import ctypes

class VkCommandBufferBeginInfo(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkDeviceGroupCommandBufferBeginInfo',
    }
    _includes_ = {
        'VkCommandBufferInheritanceInfo',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkBeginCommandBuffer',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'pInheritanceInfo': 'inheritance_info',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkCommandBufferUsageFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_COMMAND_BUFFER_BEGIN_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_COMMAND_BUFFER_BEGIN_INFO
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkCommandBufferInheritanceInfo import VkCommandBufferInheritanceInfo

VkCommandBufferBeginInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('pInheritanceInfo', ctypes.POINTER(VkCommandBufferInheritanceInfo)),
]

VkCommandBufferBeginInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'pInheritanceInfo': ctypes.POINTER(VkCommandBufferInheritanceInfo),
}
