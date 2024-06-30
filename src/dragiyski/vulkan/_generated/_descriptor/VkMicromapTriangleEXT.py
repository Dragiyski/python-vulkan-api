from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkMicromapTriangleEXT'
_member_list_ = ['dataOffset', 'subdivisionLevel', 'format']
_member_info_ = {
    'dataOffset': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'subdivisionLevel': {
        'type': CIntType('c_uint16'),
        'is_string': False,
    },
    'format': {
        'type': CIntType('c_uint16'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
