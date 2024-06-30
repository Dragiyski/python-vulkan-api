from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkExportMetalObjectCreateInfoEXT'
_member_list_ = ['sType', 'pNext', 'exportObjectType']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_EXPORT_METAL_OBJECT_CREATE_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'exportObjectType': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkExportMetalObjectTypeFlagBitsEXT',
        'is_string': False,
    },
}
_extends_ = {
    'VkBufferViewCreateInfo',
    'VkEventCreateInfo',
    'VkImageCreateInfo',
    'VkImageViewCreateInfo',
    'VkInstanceCreateInfo',
    'VkMemoryAllocateInfo',
    'VkSemaphoreCreateInfo',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
