from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDebugMarkerObjectTagInfoEXT'
_member_list_ = ['sType', 'pNext', 'objectType', 'object', 'tagName', 'tagSize', 'pTag']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_DEBUG_MARKER_OBJECT_TAG_INFO_EXT',
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
    'tagName': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'tagSize': {
        'type': CIntType('c_size_t'),
        'is_string': False,
    },
    'pTag': {
        'type': CIntType('c_void_p'),
        'length': [['tagSize']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkDebugMarkerSetObjectTagEXT',
}
_output_of_ = set()
