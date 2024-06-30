from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkMemoryMapPlacedInfoEXT'
_member_list_ = ['sType', 'pNext', 'pPlacedAddress']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_MEMORY_MAP_PLACED_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pPlacedAddress': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
}
_extends_ = {
    'VkMemoryMapInfoKHR',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
