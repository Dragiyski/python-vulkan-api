from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSemaphoreCreateInfo'
_member_list_ = ['sType', 'pNext', 'flags']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_SEMAPHORE_CREATE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkSemaphoreCreateFlags',
        'enum': 'VkSemaphoreCreateFlags',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkExportMetalObjectCreateInfoEXT',
    'VkExportSemaphoreCreateInfo',
    'VkExportSemaphoreWin32HandleInfoKHR',
    'VkImportMetalSharedEventInfoEXT',
    'VkQueryLowLatencySupportNV',
    'VkSemaphoreTypeCreateInfo',
}
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkCreateSemaphore',
}
_output_of_ = set()
