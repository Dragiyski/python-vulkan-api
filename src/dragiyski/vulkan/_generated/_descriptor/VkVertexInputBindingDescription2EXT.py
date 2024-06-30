from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVertexInputBindingDescription2EXT'
_member_list_ = ['sType', 'pNext', 'binding', 'stride', 'inputRate', 'divisor']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VERTEX_INPUT_BINDING_DESCRIPTION_2_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
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
    'divisor': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkCmdSetVertexInputEXT',
}
_output_of_ = set()
