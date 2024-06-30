from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVertexInputBindingDescription'
_member_list_ = ['binding', 'stride', 'inputRate']
_member_info_ = {
    'binding': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'stride': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'inputRate': {
        'type': CIntType('c_int'),
        'type_name': 'VkVertexInputRate',
        'enum': 'VkVertexInputRate',
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
