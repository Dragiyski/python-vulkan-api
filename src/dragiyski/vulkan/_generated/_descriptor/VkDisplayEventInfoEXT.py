from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDisplayEventInfoEXT'
_member_list_ = ['sType', 'pNext', 'displayEvent']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_DISPLAY_EVENT_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'displayEvent': {
        'type': CIntType('c_int'),
        'type_name': 'VkDisplayEventTypeEXT',
        'enum': 'VkDisplayEventTypeEXT',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkRegisterDisplayEventEXT',
}
_output_of_ = set()
