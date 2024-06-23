import ctypes

class CType(ctypes.Structure):
    pass

from .VkAttachmentReference2 import CType as VkAttachmentReference2

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('depthResolveMode', ctypes.c_uint32),
    ('stencilResolveMode', ctypes.c_uint32),
    ('pDepthStencilResolveAttachment', ctypes.POINTER(VkAttachmentReference2)),
]

descriptor = {
    'extends': {
        'VkSubpassDescription2',
    },
    'extended_by': set(),
    'includes': {
        'VkAttachmentReference2',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_SUBPASS_DESCRIPTION_DEPTH_STENCIL_RESOLVE', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'depthResolveMode': {'python_name': ['depth', 'resolve', 'mode'], 'type': 'VkResolveModeFlagBits'},
        'stencilResolveMode': {'python_name': ['stencil', 'resolve', 'mode'], 'type': 'VkResolveModeFlagBits'},
        'pDepthStencilResolveAttachment': {'python_name': ['p', 'depth', 'stencil', 'resolve', 'attachment'], 'type': 'VkAttachmentReference2'},
    }
}
