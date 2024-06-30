from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkRenderingAttachmentInfo'
_member_list_ = ['sType', 'pNext', 'imageView', 'imageLayout', 'resolveMode', 'resolveImageView', 'resolveImageLayout', 'loadOp', 'storeOp', 'clearValue']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_RENDERING_ATTACHMENT_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'imageView': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'imageLayout': {
        'type': CIntType('c_int'),
        'type_name': 'VkImageLayout',
        'enum': 'VkImageLayout',
        'is_string': False,
    },
    'resolveMode': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkResolveModeFlagBits',
        'is_string': False,
    },
    'resolveImageView': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'resolveImageLayout': {
        'type': CIntType('c_int'),
        'type_name': 'VkImageLayout',
        'enum': 'VkImageLayout',
        'is_string': False,
    },
    'loadOp': {
        'type': CIntType('c_int'),
        'type_name': 'VkAttachmentLoadOp',
        'enum': 'VkAttachmentLoadOp',
        'is_string': False,
    },
    'storeOp': {
        'type': CIntType('c_int'),
        'type_name': 'VkAttachmentStoreOp',
        'enum': 'VkAttachmentStoreOp',
        'is_string': False,
    },
    'clearValue': {
        'type': CComplexType('VkClearValue'),
        'type_name': 'VkClearValue',
        'union': 'VkClearValue',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkClearValue',
}
_included_in_ = {
    'VkRenderingInfo',
}
_input_of_ = set()
_output_of_ = set()
