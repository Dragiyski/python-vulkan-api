from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkAttachmentDescription2'
_member_list_ = ['sType', 'pNext', 'flags', 'format', 'samples', 'loadOp', 'storeOp', 'stencilLoadOp', 'stencilStoreOp', 'initialLayout', 'finalLayout']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_ATTACHMENT_DESCRIPTION_2',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
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
_extended_by_ = {
    'VkAttachmentDescriptionStencilLayout',
    'VkExternalFormatANDROID',
}
_includes_ = set()
_included_in_ = {
    'VkRenderPassCreateInfo2',
}
_input_of_ = set()
_output_of_ = set()
