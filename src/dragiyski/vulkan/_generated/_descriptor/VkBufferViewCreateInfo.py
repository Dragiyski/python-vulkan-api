from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkBufferViewCreateInfo'
_member_list_ = ['sType', 'pNext', 'flags', 'buffer', 'format', 'offset', 'range']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_BUFFER_VIEW_CREATE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkBufferViewCreateFlags',
        'enum': 'VkBufferViewCreateFlags',
        'is_string': False,
    },
    'buffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'format': {
        'type': CIntType('c_int'),
        'type_name': 'VkFormat',
        'enum': 'VkFormat',
        'is_string': False,
    },
    'offset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'range': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkBufferUsageFlags2CreateInfoKHR',
    'VkExportMetalObjectCreateInfoEXT',
}
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkCreateBufferView',
}
_output_of_ = set()
