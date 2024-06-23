import ctypes

class CType(ctypes.Structure):
    pass

from .VkImageSubresourceRange import CType as VkImageSubresourceRange

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('srcStageMask', ctypes.c_uint64),
    ('srcAccessMask', ctypes.c_uint64),
    ('dstStageMask', ctypes.c_uint64),
    ('dstAccessMask', ctypes.c_uint64),
    ('oldLayout', ctypes.c_int),
    ('newLayout', ctypes.c_int),
    ('srcQueueFamilyIndex', ctypes.c_uint32),
    ('dstQueueFamilyIndex', ctypes.c_uint32),
    ('image', ctypes.c_void_p),
    ('subresourceRange', VkImageSubresourceRange),
]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkExternalMemoryAcquireUnmodifiedEXT',
        'VkSampleLocationsInfoEXT',
    },
    'includes': {
        'VkImageSubresourceRange',
    },
    'included_in': {
        'VkDependencyInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_IMAGE_MEMORY_BARRIER_2', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'srcStageMask': {'python_name': ['src', 'stage', 'mask'], 'type': 'VkPipelineStageFlags2'},
        'srcAccessMask': {'python_name': ['src', 'access', 'mask'], 'type': 'VkAccessFlags2'},
        'dstStageMask': {'python_name': ['dst', 'stage', 'mask'], 'type': 'VkPipelineStageFlags2'},
        'dstAccessMask': {'python_name': ['dst', 'access', 'mask'], 'type': 'VkAccessFlags2'},
        'oldLayout': {'python_name': ['old', 'layout'], 'type': 'VkImageLayout'},
        'newLayout': {'python_name': ['new', 'layout'], 'type': 'VkImageLayout'},
        'srcQueueFamilyIndex': {'python_name': ['src', 'queue', 'family', 'index']},
        'dstQueueFamilyIndex': {'python_name': ['dst', 'queue', 'family', 'index']},
        'image': {'python_name': ['image']},
        'subresourceRange': {'python_name': ['subresource', 'range'], 'type': 'VkImageSubresourceRange'},
    }
}
