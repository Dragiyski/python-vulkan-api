import ctypes

class VkBufferCreateInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('size', ctypes.c_uint64),
        ('usage', ctypes.c_uint32),
        ('sharingMode', ctypes.c_int),
        ('queueFamilyIndexCount', ctypes.c_uint32),
        ('pQueueFamilyIndices', ctypes.POINTER(ctypes.c_uint32)),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkBufferCollectionBufferCreateInfoFUCHSIA',
        'VkBufferDeviceAddressCreateInfoEXT',
        'VkBufferOpaqueCaptureAddressCreateInfo',
        'VkBufferUsageFlags2CreateInfoKHR',
        'VkDedicatedAllocationBufferCreateInfoNV',
        'VkExternalMemoryBufferCreateInfo',
        'VkOpaqueCaptureDescriptorDataCreateInfoEXT',
        'VkVideoProfileListInfoKHR',
    }
    _includes_ = set()
    _included_in_ = {
        'VkBufferConstraintsInfoFUCHSIA',
        'VkDeviceBufferMemoryRequirements',
    }
    _input_of_ = {
        'vkCreateBuffer',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'size': 'size',
        'usage': 'usage',
        'sharingMode': 'sharing_mode',
        'queueFamilyIndexCount': 'queue_family_index_count',
        'pQueueFamilyIndices': 'queue_family_indices',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkBufferCreateFlags',
        'usage': 'VkBufferUsageFlags',
        'sharingMode': 'VkSharingMode',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_BUFFER_CREATE_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_BUFFER_CREATE_INFO
        for function in self._init_:
            function(self, *args, **kwargs)

VkBufferCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'size': ctypes.c_uint64,
    'usage': ctypes.c_uint32,
    'sharingMode': ctypes.c_int,
    'queueFamilyIndexCount': ctypes.c_uint32,
    'pQueueFamilyIndices': ctypes.POINTER(ctypes.c_uint32),
}
