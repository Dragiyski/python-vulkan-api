from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkRenderPassAttachmentBeginInfo'
_member_list_ = ['sType', 'pNext', 'attachmentCount', 'pAttachments']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_RENDER_PASS_ATTACHMENT_BEGIN_INFO',
        'is_string': False,
    },
    'pNext': {
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
}
_extends_ = {
    'VkRenderPassBeginInfo',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
