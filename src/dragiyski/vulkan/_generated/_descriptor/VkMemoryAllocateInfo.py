from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkMemoryAllocateInfo'
_member_list_ = ['sType', 'pNext', 'allocationSize', 'memoryTypeIndex']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_MEMORY_ALLOCATE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'allocationSize': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'memoryTypeIndex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
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
