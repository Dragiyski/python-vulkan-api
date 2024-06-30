from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSubpassDescriptionDepthStencilResolve'
_member_list_ = ['sType', 'pNext', 'depthResolveMode', 'stencilResolveMode', 'pDepthStencilResolveAttachment']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_SUBPASS_DESCRIPTION_DEPTH_STENCIL_RESOLVE',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'depthResolveMode': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkResolveModeFlagBits',
        'is_string': False,
    },
    'stencilResolveMode': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkResolveModeFlagBits',
        'is_string': False,
    },
    'pDepthStencilResolveAttachment': {
        'type': CPointerType(CComplexType('VkAttachmentReference2')),
        'type_name': 'VkAttachmentReference2',
        'structure': 'VkAttachmentReference2',
        'is_string': False,
    },
}
_extends_ = {
    'VkSubpassDescription2',
}
_extended_by_ = set()
_includes_ = {
    'VkAttachmentReference2',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
