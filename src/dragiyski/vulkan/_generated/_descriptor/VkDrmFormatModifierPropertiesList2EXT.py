from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDrmFormatModifierPropertiesList2EXT'
_member_list_ = ['sType', 'pNext', 'drmFormatModifierCount', 'pDrmFormatModifierProperties']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_DRM_FORMAT_MODIFIER_PROPERTIES_LIST_2_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'drmFormatModifierCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pDrmFormatModifierProperties': {
        'type': CPointerType(CComplexType('VkDrmFormatModifierProperties2EXT')),
        'type_name': 'VkDrmFormatModifierProperties2EXT',
        'structure': 'VkDrmFormatModifierProperties2EXT',
        'length': [['drmFormatModifierCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkFormatProperties2',
}
_extended_by_ = set()
_includes_ = {
    'VkDrmFormatModifierProperties2EXT',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
