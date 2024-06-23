import ctypes

class CType(ctypes.Structure):
    pass

from .VkFramebufferAttachmentImageInfo import CType as VkFramebufferAttachmentImageInfo

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('attachmentImageInfoCount', ctypes.c_uint32),
    ('pAttachmentImageInfos', ctypes.POINTER(VkFramebufferAttachmentImageInfo)),
]

descriptor = {
    'extends': {
        'VkFramebufferCreateInfo',
    },
    'extended_by': set(),
    'includes': {
        'VkFramebufferAttachmentImageInfo',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_FRAMEBUFFER_ATTACHMENTS_CREATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'attachmentImageInfoCount': {'python_name': ['attachment', 'image', 'info', 'count']},
        'pAttachmentImageInfos': {'python_name': ['p', 'attachment', 'image', 'infos'], 'len': [['attachmentImageInfoCount']], 'type': 'VkFramebufferAttachmentImageInfo'},
    }
}
