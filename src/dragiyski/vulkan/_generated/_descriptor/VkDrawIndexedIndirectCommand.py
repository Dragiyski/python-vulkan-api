from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDrawIndexedIndirectCommand'
_member_list_ = ['indexCount', 'instanceCount', 'firstIndex', 'vertexOffset', 'firstInstance']
_member_info_ = {
    'indexCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'instanceCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'firstIndex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'vertexOffset': {
        'type': CIntType('c_int32'),
        'is_string': False,
    },
    'firstInstance': {
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
