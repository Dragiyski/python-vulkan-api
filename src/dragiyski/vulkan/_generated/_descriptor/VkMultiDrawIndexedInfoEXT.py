from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkMultiDrawIndexedInfoEXT'
_member_list_ = ['firstIndex', 'indexCount', 'vertexOffset']
_member_info_ = {
    'firstIndex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'indexCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'vertexOffset': {
        'type': CIntType('c_int32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkCmdDrawMultiIndexedEXT',
}
_output_of_ = set()
