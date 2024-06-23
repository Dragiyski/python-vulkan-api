import ctypes

class CType(ctypes.Structure):
    pass

from .VkAttachmentReference2 import CType as VkAttachmentReference2

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('pipelineBindPoint', ctypes.c_int),
    ('viewMask', ctypes.c_uint32),
    ('inputAttachmentCount', ctypes.c_uint32),
    ('pInputAttachments', ctypes.POINTER(VkAttachmentReference2)),
    ('colorAttachmentCount', ctypes.c_uint32),
    ('pColorAttachments', ctypes.POINTER(VkAttachmentReference2)),
    ('pResolveAttachments', ctypes.POINTER(VkAttachmentReference2)),
    ('pDepthStencilAttachment', ctypes.POINTER(VkAttachmentReference2)),
    ('preserveAttachmentCount', ctypes.c_uint32),
    ('pPreserveAttachments', ctypes.POINTER(ctypes.c_uint32)),
]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkFragmentShadingRateAttachmentInfoKHR',
        'VkMultisampledRenderToSingleSampledInfoEXT',
        'VkRenderPassCreationControlEXT',
        'VkRenderPassSubpassFeedbackCreateInfoEXT',
        'VkSubpassDescriptionDepthStencilResolve',
    },
    'includes': {
        'VkAttachmentReference2',
    },
    'included_in': {
        'VkRenderPassCreateInfo2',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_SUBPASS_DESCRIPTION_2', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkSubpassDescriptionFlags'},
        'pipelineBindPoint': {'python_name': ['pipeline', 'bind', 'point'], 'type': 'VkPipelineBindPoint'},
        'viewMask': {'python_name': ['view', 'mask']},
        'inputAttachmentCount': {'python_name': ['input', 'attachment', 'count']},
        'pInputAttachments': {'python_name': ['p', 'input', 'attachments'], 'len': [['inputAttachmentCount']], 'type': 'VkAttachmentReference2'},
        'colorAttachmentCount': {'python_name': ['color', 'attachment', 'count']},
        'pColorAttachments': {'python_name': ['p', 'color', 'attachments'], 'len': [['colorAttachmentCount']], 'type': 'VkAttachmentReference2'},
        'pResolveAttachments': {'python_name': ['p', 'resolve', 'attachments'], 'len': [['colorAttachmentCount']], 'type': 'VkAttachmentReference2'},
        'pDepthStencilAttachment': {'python_name': ['p', 'depth', 'stencil', 'attachment'], 'type': 'VkAttachmentReference2'},
        'preserveAttachmentCount': {'python_name': ['preserve', 'attachment', 'count']},
        'pPreserveAttachments': {'python_name': ['p', 'preserve', 'attachments'], 'len': [['preserveAttachmentCount']]},
    }
}
