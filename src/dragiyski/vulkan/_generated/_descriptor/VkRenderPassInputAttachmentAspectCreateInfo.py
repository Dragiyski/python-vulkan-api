from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkRenderPassInputAttachmentAspectCreateInfo'
_member_list_ = ['sType', 'pNext', 'aspectReferenceCount', 'pAspectReferences']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_RENDER_PASS_INPUT_ATTACHMENT_ASPECT_CREATE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'aspectReferenceCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pAspectReferences': {
        'type': CPointerType(CComplexType('VkInputAttachmentAspectReference')),
        'type_name': 'VkInputAttachmentAspectReference',
        'structure': 'VkInputAttachmentAspectReference',
        'length': [['aspectReferenceCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkRenderPassCreateInfo',
}
_extended_by_ = set()
_includes_ = {
    'VkInputAttachmentAspectReference',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
