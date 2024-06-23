import ctypes

class CType(ctypes.Structure):
    pass

from .VkInputAttachmentAspectReference import CType as VkInputAttachmentAspectReference

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('aspectReferenceCount', ctypes.c_uint32),
    ('pAspectReferences', ctypes.POINTER(VkInputAttachmentAspectReference)),
]

descriptor = {
    'extends': {
        'VkRenderPassCreateInfo',
    },
    'extended_by': set(),
    'includes': {
        'VkInputAttachmentAspectReference',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_RENDER_PASS_INPUT_ATTACHMENT_ASPECT_CREATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'aspectReferenceCount': {'python_name': ['aspect', 'reference', 'count']},
        'pAspectReferences': {'python_name': ['p', 'aspect', 'references'], 'len': [['aspectReferenceCount']], 'type': 'VkInputAttachmentAspectReference'},
    }
}
