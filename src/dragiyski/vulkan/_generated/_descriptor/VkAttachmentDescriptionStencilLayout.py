from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkAttachmentDescriptionStencilLayout'
_member_list_ = ['sType', 'pNext', 'stencilInitialLayout', 'stencilFinalLayout']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_ATTACHMENT_DESCRIPTION_STENCIL_LAYOUT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'stencilInitialLayout': {
        'type': CIntType('c_int'),
        'type_name': 'VkImageLayout',
        'enum': 'VkImageLayout',
        'is_string': False,
    },
    'stencilFinalLayout': {
        'type': CIntType('c_int'),
        'type_name': 'VkImageLayout',
        'enum': 'VkImageLayout',
        'is_string': False,
    },
}
_extends_ = {
    'VkAttachmentDescription2',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
