from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkMultiDrawInfoEXT'
_member_list_ = ['firstVertex', 'vertexCount']
_member_info_ = {
    'firstVertex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'vertexCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkCmdDrawMultiEXT',
}
_output_of_ = set()
