import ctypes

class CType(ctypes.Union):
    pass

from .VkClearColorValue import CType as VkClearColorValue
from .VkClearDepthStencilValue import CType as VkClearDepthStencilValue

CType._fields_ = [
    ('color', VkClearColorValue),
    ('depthStencil', VkClearDepthStencilValue),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkClearColorValue',
        'VkClearDepthStencilValue',
    },
    'included_in': {
        'VkClearAttachment',
        'VkRenderPassBeginInfo',
        'VkRenderingAttachmentInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'color': {'python_name': ['color'], 'type': 'VkClearColorValue'},
        'depthStencil': {'python_name': ['depth', 'stencil'], 'type': 'VkClearDepthStencilValue'},
    }
}
