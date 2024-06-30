from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkShaderModuleIdentifierEXT'
_member_list_ = ['sType', 'pNext', 'identifierSize', 'identifier']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_SHADER_MODULE_IDENTIFIER_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'identifierSize': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'identifier': {
        'type': CArrayType(CIntType('c_uint8'), 32),
        'length': [['identifierSize']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = {
    'vkGetShaderModuleCreateInfoIdentifierEXT',
    'vkGetShaderModuleIdentifierEXT',
}
