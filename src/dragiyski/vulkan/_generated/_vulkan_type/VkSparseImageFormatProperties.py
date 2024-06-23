import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent3D import CType as VkExtent3D

CType._fields_ = [
    ('aspectMask', ctypes.c_uint32),
    ('imageGranularity', VkExtent3D),
    ('flags', ctypes.c_uint32),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkExtent3D',
    },
    'included_in': {
        'VkSparseImageFormatProperties2',
        'VkSparseImageMemoryRequirements',
    },
    'input_of': set(),
    'output_of': {
        'vkGetPhysicalDeviceSparseImageFormatProperties',
    },
    'member_map': {
        'aspectMask': {'python_name': ['aspect', 'mask'], 'type': 'VkImageAspectFlags'},
        'imageGranularity': {'python_name': ['image', 'granularity'], 'type': 'VkExtent3D'},
        'flags': {'python_name': ['flags'], 'type': 'VkSparseImageFormatFlags'},
    }
}
