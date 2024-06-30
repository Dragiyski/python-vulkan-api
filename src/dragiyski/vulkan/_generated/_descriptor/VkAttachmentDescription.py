from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkAttachmentDescription'
_member_list_ = ['flags', 'format', 'samples', 'loadOp', 'storeOp', 'stencilLoadOp', 'stencilStoreOp', 'initialLayout', 'finalLayout']
_member_info_ = {
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkAttachmentDescriptionFlags',
        'enum': 'VkAttachmentDescriptionFlags',
        'is_string': False,
    },
    'format': {
        'type': CIntType('c_int'),
        'type_name': 'VkFormat',
        'enum': 'VkFormat',
        'is_string': False,
    },
    'samples': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkSampleCountFlagBits',
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
    'stencilLoadOp': {
        'type': CIntType('c_int'),
        'type_name': 'VkAttachmentLoadOp',
        'enum': 'VkAttachmentLoadOp',
        'is_string': False,
    },
    'stencilStoreOp': {
        'type': CIntType('c_int'),
        'type_name': 'VkAttachmentStoreOp',
        'enum': 'VkAttachmentStoreOp',
        'is_string': False,
    },
    'initialLayout': {
        'type': CIntType('c_int'),
        'type_name': 'VkImageLayout',
        'enum': 'VkImageLayout',
        'is_string': False,
    },
    'finalLayout': {
        'type': CIntType('c_int'),
        'type_name': 'VkImageLayout',
        'enum': 'VkImageLayout',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkRenderPassCreateInfo',
}
_input_of_ = set()
_output_of_ = set()
