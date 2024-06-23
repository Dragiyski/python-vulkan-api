import ctypes

class CType(ctypes.Structure):
    pass

from .VkRect2D import CType as VkRect2D
from .VkRenderingAttachmentInfo import CType as VkRenderingAttachmentInfo

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('renderArea', VkRect2D),
    ('layerCount', ctypes.c_uint32),
    ('viewMask', ctypes.c_uint32),
    ('colorAttachmentCount', ctypes.c_uint32),
    ('pColorAttachments', ctypes.POINTER(VkRenderingAttachmentInfo)),
    ('pDepthAttachment', ctypes.POINTER(VkRenderingAttachmentInfo)),
    ('pStencilAttachment', ctypes.POINTER(VkRenderingAttachmentInfo)),
]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkDeviceGroupRenderPassBeginInfo',
        'VkMultisampledRenderToSingleSampledInfoEXT',
        'VkMultiviewPerViewAttributesInfoNVX',
        'VkMultiviewPerViewRenderAreasRenderPassBeginInfoQCOM',
        'VkRenderPassStripeBeginInfoARM',
        'VkRenderingFragmentDensityMapAttachmentInfoEXT',
        'VkRenderingFragmentShadingRateAttachmentInfoKHR',
    },
    'includes': {
        'VkRect2D',
        'VkRenderingAttachmentInfo',
    },
    'included_in': set(),
    'input_of': {
        'vkCmdBeginRendering',
        'vkGetDynamicRenderingTilePropertiesQCOM',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_RENDERING_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkRenderingFlags'},
        'renderArea': {'python_name': ['render', 'area'], 'type': 'VkRect2D'},
        'layerCount': {'python_name': ['layer', 'count']},
        'viewMask': {'python_name': ['view', 'mask']},
        'colorAttachmentCount': {'python_name': ['color', 'attachment', 'count']},
        'pColorAttachments': {'python_name': ['p', 'color', 'attachments'], 'len': [['colorAttachmentCount']], 'type': 'VkRenderingAttachmentInfo'},
        'pDepthAttachment': {'python_name': ['p', 'depth', 'attachment'], 'type': 'VkRenderingAttachmentInfo'},
        'pStencilAttachment': {'python_name': ['p', 'stencil', 'attachment'], 'type': 'VkRenderingAttachmentInfo'},
    }
}
