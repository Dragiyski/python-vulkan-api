import ctypes

class VkDescriptorBufferBindingInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('address', ctypes.c_uint64),
        ('usage', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkBufferUsageFlags2CreateInfoKHR',
        'VkDescriptorBufferBindingPushDescriptorBufferHandleEXT',
    }
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkCmdBindDescriptorBuffersEXT',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'address': 'address',
        'usage': 'usage',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_descriptor_buffer',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'usage': 'VkBufferUsageFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_DESCRIPTOR_BUFFER_BINDING_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_DESCRIPTOR_BUFFER_BINDING_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkDescriptorBufferBindingInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'address': ctypes.c_uint64,
    'usage': ctypes.c_uint32,
}
