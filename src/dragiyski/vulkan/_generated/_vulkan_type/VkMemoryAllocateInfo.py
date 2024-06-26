import ctypes

class VkMemoryAllocateInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('allocationSize', ctypes.c_uint64),
        ('memoryTypeIndex', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkDedicatedAllocationMemoryAllocateInfoNV',
        'VkExportMemoryAllocateInfo',
        'VkExportMemoryAllocateInfoNV',
        'VkExportMemoryWin32HandleInfoKHR',
        'VkExportMemoryWin32HandleInfoNV',
        'VkExportMetalObjectCreateInfoEXT',
        'VkImportAndroidHardwareBufferInfoANDROID',
        'VkImportMemoryBufferCollectionFUCHSIA',
        'VkImportMemoryFdInfoKHR',
        'VkImportMemoryHostPointerInfoEXT',
        'VkImportMemoryWin32HandleInfoKHR',
        'VkImportMemoryWin32HandleInfoNV',
        'VkImportMemoryZirconHandleInfoFUCHSIA',
        'VkImportMetalBufferInfoEXT',
        'VkImportScreenBufferInfoQNX',
        'VkMemoryAllocateFlagsInfo',
        'VkMemoryDedicatedAllocateInfo',
        'VkMemoryOpaqueCaptureAddressAllocateInfo',
        'VkMemoryPriorityAllocateInfoEXT',
    }
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkAllocateMemory',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'allocationSize': 'allocation_size',
        'memoryTypeIndex': 'memory_type_index',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_MEMORY_ALLOCATE_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_MEMORY_ALLOCATE_INFO
        for function in self._init_:
            function(self, *args, **kwargs)

VkMemoryAllocateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'allocationSize': ctypes.c_uint64,
    'memoryTypeIndex': ctypes.c_uint32,
}
