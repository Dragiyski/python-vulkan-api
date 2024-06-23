import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('allocationSize', ctypes.c_uint64),
        ('memoryTypeIndex', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkDedicatedAllocationMemoryAllocateInfoNV',
        'VkExportMemoryAllocateInfo',
        'VkExportMemoryAllocateInfoNV',
        'VkExportMemorySciBufInfoNV',
        'VkExportMemoryWin32HandleInfoKHR',
        'VkExportMemoryWin32HandleInfoNV',
        'VkExportMetalObjectCreateInfoEXT',
        'VkImportAndroidHardwareBufferInfoANDROID',
        'VkImportMemoryBufferCollectionFUCHSIA',
        'VkImportMemoryFdInfoKHR',
        'VkImportMemoryHostPointerInfoEXT',
        'VkImportMemorySciBufInfoNV',
        'VkImportMemoryWin32HandleInfoKHR',
        'VkImportMemoryWin32HandleInfoNV',
        'VkImportMemoryZirconHandleInfoFUCHSIA',
        'VkImportMetalBufferInfoEXT',
        'VkImportScreenBufferInfoQNX',
        'VkMemoryAllocateFlagsInfo',
        'VkMemoryDedicatedAllocateInfo',
        'VkMemoryOpaqueCaptureAddressAllocateInfo',
        'VkMemoryPriorityAllocateInfoEXT',
    },
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkAllocateMemory',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_MEMORY_ALLOCATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'allocationSize': {'python_name': ['allocation', 'size']},
        'memoryTypeIndex': {'python_name': ['memory', 'type', 'index']},
    }
}
