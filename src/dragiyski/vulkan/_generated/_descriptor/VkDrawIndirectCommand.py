from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDrawIndirectCommand'
_member_list_ = ['vertexCount', 'instanceCount', 'firstVertex', 'firstInstance']
_member_info_ = {
    'vertexCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'instanceCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'firstVertex': {
        'type': CIntType('c_uint32'),
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
