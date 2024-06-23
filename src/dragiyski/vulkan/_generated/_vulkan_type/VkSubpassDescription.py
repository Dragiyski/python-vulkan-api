import ctypes

class CType(ctypes.Structure):
    pass

from .VkAttachmentReference import CType as VkAttachmentReference

CType._fields_ = [
    ('flags', ctypes.c_uint32),
    ('pipelineBindPoint', ctypes.c_int),
    ('inputAttachmentCount', ctypes.c_uint32),
    ('pInputAttachments', ctypes.POINTER(VkAttachmentReference)),
    ('colorAttachmentCount', ctypes.c_uint32),
    ('pColorAttachments', ctypes.POINTER(VkAttachmentReference)),
    ('pResolveAttachments', ctypes.POINTER(VkAttachmentReference)),
    ('pDepthStencilAttachment', ctypes.POINTER(VkAttachmentReference)),
    ('preserveAttachmentCount', ctypes.c_uint32),
    ('pPreserveAttachments', ctypes.POINTER(ctypes.c_uint32)),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkAttachmentReference',
    },
    'included_in': {
        'VkRenderPassCreateInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'flags': {'python_name': ['flags'], 'type': 'VkSubpassDescriptionFlags'},
        'pipelineBindPoint': {'python_name': ['pipeline', 'bind', 'point'], 'type': 'VkPipelineBindPoint'},
        'inputAttachmentCount': {'python_name': ['input', 'attachment', 'count']},
        'pInputAttachments': {'python_name': ['p', 'input', 'attachments'], 'len': [['inputAttachmentCount']], 'type': 'VkAttachmentReference'},
        'colorAttachmentCount': {'python_name': ['color', 'attachment', 'count']},
        'pColorAttachments': {'python_name': ['p', 'color', 'attachments'], 'len': [['colorAttachmentCount']], 'type': 'VkAttachmentReference'},
        'pResolveAttachments': {'python_name': ['p', 'resolve', 'attachments'], 'len': [['colorAttachmentCount']], 'type': 'VkAttachmentReference'},
        'pDepthStencilAttachment': {'python_name': ['p', 'depth', 'stencil', 'attachment'], 'type': 'VkAttachmentReference'},
        'preserveAttachmentCount': {'python_name': ['preserve', 'attachment', 'count']},
        'pPreserveAttachments': {'python_name': ['p', 'preserve', 'attachments'], 'len': [['preserveAttachmentCount']]},
    }
}
