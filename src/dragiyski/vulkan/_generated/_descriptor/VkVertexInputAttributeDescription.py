from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVertexInputAttributeDescription'
_member_list_ = ['location', 'binding', 'format', 'offset']
_member_info_ = {
    'location': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'binding': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'format': {
        'type': CIntType('c_int'),
        'type_name': 'VkFormat',
        'enum': 'VkFormat',
        'is_string': False,
    },
    'offset': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkPipelineVertexInputStateCreateInfo',
}
_input_of_ = set()
_output_of_ = set()
