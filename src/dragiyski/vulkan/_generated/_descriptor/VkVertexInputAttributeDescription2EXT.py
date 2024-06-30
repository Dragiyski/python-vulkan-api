from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVertexInputAttributeDescription2EXT'
_member_list_ = ['sType', 'pNext', 'location', 'binding', 'format', 'offset']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VERTEX_INPUT_ATTRIBUTE_DESCRIPTION_2_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
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
_included_in_ = set()
_input_of_ = {
    'vkCmdSetVertexInputEXT',
}
_output_of_ = set()
