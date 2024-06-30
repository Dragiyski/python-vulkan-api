from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDescriptorBufferBindingInfoEXT'
_member_list_ = ['sType', 'pNext', 'address', 'usage']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_DESCRIPTOR_BUFFER_BINDING_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'address': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'usage': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkBufferUsageFlags',
        'enum': 'VkBufferUsageFlags',
        'is_string': False,
    },
}
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
