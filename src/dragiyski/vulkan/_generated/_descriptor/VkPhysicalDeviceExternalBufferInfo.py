from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceExternalBufferInfo'
_member_list_ = ['sType', 'pNext', 'flags', 'usage', 'handleType']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTERNAL_BUFFER_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkBufferCreateFlags',
        'enum': 'VkBufferCreateFlags',
        'is_string': False,
    },
    'usage': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkBufferUsageFlags',
        'enum': 'VkBufferUsageFlags',
        'is_string': False,
    },
    'handleType': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkExternalMemoryHandleTypeFlagBits',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkBufferUsageFlags2CreateInfoKHR',
}
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkGetPhysicalDeviceExternalBufferProperties',
}
_output_of_ = set()
