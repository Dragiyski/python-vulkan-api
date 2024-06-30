from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkBufferUsageFlags2CreateInfoKHR'
_member_list_ = ['sType', 'pNext', 'usage']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_BUFFER_USAGE_FLAGS_2_CREATE_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'usage': {
        'type': CIntType('c_uint64'),
        'type_name': 'VkBufferUsageFlags2KHR',
        'enum': 'VkBufferUsageFlags2KHR',
        'is_string': False,
    },
}
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
