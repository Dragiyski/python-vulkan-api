import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('aspectMask', ctypes.c_uint32),
        ('mipLevel', ctypes.c_uint32),
        ('arrayLayer', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkImageSubresource2KHR',
        'VkSparseImageMemoryBind',
    },
    'input_of': {
        'vkGetImageSubresourceLayout',
    },
    'output_of': set(),
    'member_map': {
        'aspectMask': {'python_name': ['aspect', 'mask'], 'type': 'VkImageAspectFlags'},
        'mipLevel': {'python_name': ['mip', 'level']},
        'arrayLayer': {'python_name': ['array', 'layer']},
    }
}
