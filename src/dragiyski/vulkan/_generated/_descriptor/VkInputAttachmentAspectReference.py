from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkInputAttachmentAspectReference'
_member_list_ = ['subpass', 'inputAttachmentIndex', 'aspectMask']
_member_info_ = {
    'subpass': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'inputAttachmentIndex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'aspectMask': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkImageAspectFlags',
        'enum': 'VkImageAspectFlags',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkRenderPassInputAttachmentAspectCreateInfo',
}
_input_of_ = set()
_output_of_ = set()
