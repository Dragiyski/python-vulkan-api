from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSysmemColorSpaceFUCHSIA'
_member_list_ = ['sType', 'pNext', 'colorSpace']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_SYSMEM_COLOR_SPACE_FUCHSIA',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'colorSpace': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkBufferCollectionPropertiesFUCHSIA',
    'VkImageFormatConstraintsInfoFUCHSIA',
}
_input_of_ = set()
_output_of_ = set()
