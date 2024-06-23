import ctypes

class CType(ctypes.Structure):
    pass

from .VkImageSubresourceLayers import CType as VkImageSubresourceLayers
from .VkOffset3D import CType as VkOffset3D

CType._fields_ = [
    ('srcSubresource', VkImageSubresourceLayers),
    ('srcOffsets', ctypes.ARRAY(VkOffset3D, 2)),
    ('dstSubresource', VkImageSubresourceLayers),
    ('dstOffsets', ctypes.ARRAY(VkOffset3D, 2)),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkImageSubresourceLayers',
        'VkOffset3D',
    },
    'included_in': set(),
    'input_of': {
        'vkCmdBlitImage',
    },
    'output_of': set(),
    'member_map': {
        'srcSubresource': {'python_name': ['src', 'subresource'], 'type': 'VkImageSubresourceLayers'},
        'srcOffsets': {'python_name': ['src', 'offsets'], 'type': 'VkOffset3D'},
        'dstSubresource': {'python_name': ['dst', 'subresource'], 'type': 'VkImageSubresourceLayers'},
        'dstOffsets': {'python_name': ['dst', 'offsets'], 'type': 'VkOffset3D'},
    }
}
