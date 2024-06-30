from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceShaderModuleIdentifierPropertiesEXT'
_member_list_ = ['sType', 'pNext', 'shaderModuleIdentifierAlgorithmUUID']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_MODULE_IDENTIFIER_PROPERTIES_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'shaderModuleIdentifierAlgorithmUUID': {
        'type': CArrayType(CIntType('c_uint8'), 16),
        'is_string': False,
    },
}
_extends_ = {
    'VkPhysicalDeviceProperties2',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
