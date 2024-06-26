import ctypes

class VkBufferUsageFlags2CreateInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('usage', ctypes.c_uint64),
    ]

    _init_ = []
    _extends_ = {
        'VkBufferCreateInfo',
        'VkBufferViewCreateInfo',
        'VkDescriptorBufferBindingInfoEXT',
        'VkPhysicalDeviceExternalBufferInfo',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'usage': 'usage',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_maintenance5',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'usage': 'VkBufferUsageFlags2KHR',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_BUFFER_USAGE_FLAGS_2_CREATE_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_BUFFER_USAGE_FLAGS_2_CREATE_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkBufferUsageFlags2CreateInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'usage': ctypes.c_uint64,
}
