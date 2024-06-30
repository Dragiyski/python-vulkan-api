from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDebugMarkerMarkerInfoEXT'
_member_list_ = ['sType', 'pNext', 'pMarkerName', 'color']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_DEBUG_MARKER_MARKER_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pMarkerName': {
        'type': CStringType('c_char_p'),
        'length': [],
        'is_string': True,
    },
    'color': {
        'type': CArrayType(CFloatType('c_float'), 4),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkCmdDebugMarkerBeginEXT',
    'vkCmdDebugMarkerInsertEXT',
}
_output_of_ = set()
