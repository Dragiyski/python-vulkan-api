import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent3D import CType as VkExtent3D
from .VkImageSubresourceLayers import CType as VkImageSubresourceLayers
from .VkOffset3D import CType as VkOffset3D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('srcSubresource', VkImageSubresourceLayers),
    ('srcOffset', VkOffset3D),
    ('dstSubresource', VkImageSubresourceLayers),
    ('dstOffset', VkOffset3D),
    ('extent', VkExtent3D),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkExtent3D',
        'VkImageSubresourceLayers',
        'VkOffset3D',
    },
    'included_in': {
        'VkCopyImageInfo2',
        'VkCopyImageToImageInfoEXT',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_IMAGE_COPY_2', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'srcSubresource': {'python_name': ['src', 'subresource'], 'type': 'VkImageSubresourceLayers'},
        'srcOffset': {'python_name': ['src', 'offset'], 'type': 'VkOffset3D'},
        'dstSubresource': {'python_name': ['dst', 'subresource'], 'type': 'VkImageSubresourceLayers'},
        'dstOffset': {'python_name': ['dst', 'offset'], 'type': 'VkOffset3D'},
        'extent': {'python_name': ['extent'], 'type': 'VkExtent3D'},
    }
}
