from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkMicromapCreateInfoEXT'
_member_list_ = ['sType', 'pNext', 'createFlags', 'buffer', 'offset', 'size', 'type', 'deviceAddress']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_MICROMAP_CREATE_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'createFlags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkMicromapCreateFlagsEXT',
        'enum': 'VkMicromapCreateFlagsEXT',
        'is_string': False,
    },
    'buffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'offset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'size': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'type': {
        'type': CIntType('c_int'),
        'type_name': 'VkMicromapTypeEXT',
        'enum': 'VkMicromapTypeEXT',
        'is_string': False,
    },
    'deviceAddress': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkCreateMicromapEXT',
}
_output_of_ = set()
