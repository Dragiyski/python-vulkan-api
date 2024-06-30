from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDrawMeshTasksIndirectCommandNV'
_member_list_ = ['taskCount', 'firstTask']
_member_info_ = {
    'taskCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'firstTask': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
