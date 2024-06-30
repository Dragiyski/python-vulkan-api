from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkImageDrmFormatModifierExplicitCreateInfoEXT'
_member_list_ = ['sType', 'pNext', 'drmFormatModifier', 'drmFormatModifierPlaneCount', 'pPlaneLayouts']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_IMAGE_DRM_FORMAT_MODIFIER_EXPLICIT_CREATE_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'drmFormatModifier': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'drmFormatModifierPlaneCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pPlaneLayouts': {
        'type': CPointerType(CComplexType('VkSubresourceLayout')),
        'type_name': 'VkSubresourceLayout',
        'structure': 'VkSubresourceLayout',
        'length': [['drmFormatModifierPlaneCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkImageCreateInfo',
}
_extended_by_ = set()
_includes_ = {
    'VkSubresourceLayout',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
