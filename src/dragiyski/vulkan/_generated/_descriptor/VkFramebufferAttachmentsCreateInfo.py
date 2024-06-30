from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkFramebufferAttachmentsCreateInfo'
_member_list_ = ['sType', 'pNext', 'attachmentImageInfoCount', 'pAttachmentImageInfos']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_FRAMEBUFFER_ATTACHMENTS_CREATE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'attachmentImageInfoCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pAttachmentImageInfos': {
        'type': CPointerType(CComplexType('VkFramebufferAttachmentImageInfo')),
        'type_name': 'VkFramebufferAttachmentImageInfo',
        'structure': 'VkFramebufferAttachmentImageInfo',
        'length': [['attachmentImageInfoCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkFramebufferCreateInfo',
}
_extended_by_ = set()
_includes_ = {
    'VkFramebufferAttachmentImageInfo',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
