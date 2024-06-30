from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDebugMarkerObjectNameInfoEXT'
_member_list_ = ['sType', 'pNext', 'objectType', 'object', 'pObjectName']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_DEBUG_MARKER_OBJECT_NAME_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'objectType': {
        'type': CIntType('c_int'),
        'type_name': 'VkDebugReportObjectTypeEXT',
        'enum': 'VkDebugReportObjectTypeEXT',
        'is_string': False,
    },
    'object': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'pObjectName': {
        'type': CStringType('c_char_p'),
        'length': [],
        'is_string': True,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkDebugMarkerSetObjectNameEXT',
}
_output_of_ = set()
