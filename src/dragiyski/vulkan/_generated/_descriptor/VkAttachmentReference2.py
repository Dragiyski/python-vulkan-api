from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkAttachmentReference2'
_member_list_ = ['sType', 'pNext', 'attachment', 'layout', 'aspectMask']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_ATTACHMENT_REFERENCE_2',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'attachment': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'layout': {
        'type': CIntType('c_int'),
        'type_name': 'VkImageLayout',
        'enum': 'VkImageLayout',
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
_extended_by_ = {
    'VkAttachmentReferenceStencilLayout',
}
_includes_ = set()
_included_in_ = {
    'VkFragmentShadingRateAttachmentInfoKHR',
    'VkSubpassDescription2',
    'VkSubpassDescriptionDepthStencilResolve',
}
_input_of_ = set()
_output_of_ = set()
