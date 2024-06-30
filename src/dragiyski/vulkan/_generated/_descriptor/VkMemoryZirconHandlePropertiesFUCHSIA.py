from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkMemoryZirconHandlePropertiesFUCHSIA'
_member_list_ = ['sType', 'pNext', 'memoryTypeBits']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_MEMORY_ZIRCON_HANDLE_PROPERTIES_FUCHSIA',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'memoryTypeBits': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = {
    'vkGetMemoryZirconHandlePropertiesFUCHSIA',
}
