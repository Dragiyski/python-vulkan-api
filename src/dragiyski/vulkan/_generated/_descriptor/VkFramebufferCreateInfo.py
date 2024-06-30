from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkFramebufferCreateInfo'
_member_list_ = ['sType', 'pNext', 'flags', 'renderPass', 'attachmentCount', 'pAttachments', 'width', 'height', 'layers']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_FRAMEBUFFER_CREATE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkFramebufferCreateFlags',
        'enum': 'VkFramebufferCreateFlags',
        'is_string': False,
    },
    'renderPass': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'attachmentCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pAttachments': {
        'type': CPointerType(CIntType('c_void_p')),
        'length': [['attachmentCount']],
        'is_string': False,
    },
    'width': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'height': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'layers': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkFramebufferAttachmentsCreateInfo',
}
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkCreateFramebuffer',
}
_output_of_ = set()
