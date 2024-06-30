from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoInlineQueryInfoKHR'
_member_list_ = ['sType', 'pNext', 'queryPool', 'firstQuery', 'queryCount']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_INLINE_QUERY_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'queryPool': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'firstQuery': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'queryCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = {
    'VkVideoDecodeInfoKHR',
    'VkVideoEncodeInfoKHR',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
