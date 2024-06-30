from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkValidationCacheCreateInfoEXT'
_member_list_ = ['sType', 'pNext', 'flags', 'initialDataSize', 'pInitialData']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VALIDATION_CACHE_CREATE_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkValidationCacheCreateFlagsEXT',
        'enum': 'VkValidationCacheCreateFlagsEXT',
        'is_string': False,
    },
    'initialDataSize': {
        'type': CIntType('c_size_t'),
        'is_string': False,
    },
    'pInitialData': {
        'type': CIntType('c_void_p'),
        'length': [['initialDataSize']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkCreateValidationCacheEXT',
}
_output_of_ = set()
