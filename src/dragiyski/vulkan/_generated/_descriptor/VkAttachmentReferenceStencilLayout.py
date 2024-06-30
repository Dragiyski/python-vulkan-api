from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkAttachmentReferenceStencilLayout'
_member_list_ = ['sType', 'pNext', 'stencilLayout']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_ATTACHMENT_REFERENCE_STENCIL_LAYOUT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'stencilLayout': {
        'type': CIntType('c_int'),
        'type_name': 'VkImageLayout',
        'enum': 'VkImageLayout',
        'is_string': False,
    },
}
_extends_ = {
    'VkAttachmentReference2',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
