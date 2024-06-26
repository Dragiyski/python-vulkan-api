import ctypes

class VkCommandBufferAllocateInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('commandPool', ctypes.c_void_p),
        ('level', ctypes.c_int),
        ('commandBufferCount', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkAllocateCommandBuffers',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'commandPool': 'command_pool',
        'level': 'level',
        'commandBufferCount': 'command_buffer_count',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'level': 'VkCommandBufferLevel',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_COMMAND_BUFFER_ALLOCATE_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_COMMAND_BUFFER_ALLOCATE_INFO
        for function in self._init_:
            function(self, *args, **kwargs)

VkCommandBufferAllocateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'commandPool': ctypes.c_void_p,
    'level': ctypes.c_int,
    'commandBufferCount': ctypes.c_uint32,
}
