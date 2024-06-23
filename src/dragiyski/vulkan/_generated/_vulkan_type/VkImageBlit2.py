import ctypes

class CType(ctypes.Structure):
    pass

from .VkImageSubresourceLayers import CType as VkImageSubresourceLayers
from .VkOffset3D import CType as VkOffset3D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('srcSubresource', VkImageSubresourceLayers),
    ('srcOffsets', ctypes.ARRAY(VkOffset3D, 2)),
    ('dstSubresource', VkImageSubresourceLayers),
    ('dstOffsets', ctypes.ARRAY(VkOffset3D, 2)),
]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkCopyCommandTransformInfoQCOM',
    },
    'includes': {
        'VkImageSubresourceLayers',
        'VkOffset3D',
    },
    'included_in': {
        'VkBlitImageInfo2',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_IMAGE_BLIT_2', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'srcSubresource': {'python_name': ['src', 'subresource'], 'type': 'VkImageSubresourceLayers'},
        'srcOffsets': {'python_name': ['src', 'offsets'], 'type': 'VkOffset3D'},
        'dstSubresource': {'python_name': ['dst', 'subresource'], 'type': 'VkImageSubresourceLayers'},
        'dstOffsets': {'python_name': ['dst', 'offsets'], 'type': 'VkOffset3D'},
    }
}
