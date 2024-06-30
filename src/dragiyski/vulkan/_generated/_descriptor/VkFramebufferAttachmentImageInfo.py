from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkFramebufferAttachmentImageInfo'
_member_list_ = ['sType', 'pNext', 'flags', 'usage', 'width', 'height', 'layerCount', 'viewFormatCount', 'pViewFormats']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_FRAMEBUFFER_ATTACHMENT_IMAGE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkImageCreateFlags',
        'enum': 'VkImageCreateFlags',
        'is_string': False,
    },
    'usage': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkImageUsageFlags',
        'enum': 'VkImageUsageFlags',
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
    'layerCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'viewFormatCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pViewFormats': {
        'type': CPointerType(CIntType('c_int')),
        'type_name': 'VkFormat',
        'enum': 'VkFormat',
        'length': [['viewFormatCount']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkFramebufferAttachmentsCreateInfo',
}
_input_of_ = set()
_output_of_ = set()
