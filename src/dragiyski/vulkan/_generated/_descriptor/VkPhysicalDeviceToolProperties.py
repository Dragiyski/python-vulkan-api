from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceToolProperties'
_member_list_ = ['sType', 'pNext', 'name', 'version', 'purposes', 'description', 'layer']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TOOL_PROPERTIES',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'name': {
        'type': CArrayType(CCharType('c_char'), 256),
        'length': [],
        'is_string': True,
    },
    'version': {
        'type': CArrayType(CCharType('c_char'), 256),
        'length': [],
        'is_string': True,
    },
    'purposes': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkToolPurposeFlags',
        'enum': 'VkToolPurposeFlags',
        'is_string': False,
    },
    'description': {
        'type': CArrayType(CCharType('c_char'), 256),
        'length': [],
        'is_string': True,
    },
    'layer': {
        'type': CArrayType(CCharType('c_char'), 256),
        'length': [],
        'is_string': True,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = {
    'vkGetPhysicalDeviceToolProperties',
}
