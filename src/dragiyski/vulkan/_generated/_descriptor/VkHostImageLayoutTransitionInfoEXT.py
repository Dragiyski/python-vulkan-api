from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkHostImageLayoutTransitionInfoEXT'
_member_list_ = ['sType', 'pNext', 'image', 'oldLayout', 'newLayout', 'subresourceRange']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_HOST_IMAGE_LAYOUT_TRANSITION_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'image': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'oldLayout': {
        'type': CIntType('c_int'),
        'type_name': 'VkImageLayout',
        'enum': 'VkImageLayout',
        'is_string': False,
    },
    'newLayout': {
        'type': CIntType('c_int'),
        'type_name': 'VkImageLayout',
        'enum': 'VkImageLayout',
        'is_string': False,
    },
    'subresourceRange': {
        'type': CComplexType('VkImageSubresourceRange'),
        'type_name': 'VkImageSubresourceRange',
        'structure': 'VkImageSubresourceRange',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkImageSubresourceRange',
}
_included_in_ = set()
_input_of_ = {
    'vkTransitionImageLayoutEXT',
}
_output_of_ = set()
