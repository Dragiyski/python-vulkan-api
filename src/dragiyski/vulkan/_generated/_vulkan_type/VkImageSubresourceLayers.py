import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('aspectMask', ctypes.c_uint32),
        ('mipLevel', ctypes.c_uint32),
        ('baseArrayLayer', ctypes.c_uint32),
        ('layerCount', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkBufferImageCopy',
        'VkBufferImageCopy2',
        'VkCopyMemoryToImageIndirectCommandNV',
        'VkImageBlit',
        'VkImageBlit2',
        'VkImageCopy',
        'VkImageCopy2',
        'VkImageResolve',
        'VkImageResolve2',
        'VkImageToMemoryCopyEXT',
        'VkMemoryToImageCopyEXT',
    },
    'input_of': {
        'vkCmdCopyMemoryToImageIndirectNV',
    },
    'output_of': set(),
    'member_map': {
        'aspectMask': {'python_name': ['aspect', 'mask'], 'type': 'VkImageAspectFlags'},
        'mipLevel': {'python_name': ['mip', 'level']},
        'baseArrayLayer': {'python_name': ['base', 'array', 'layer']},
        'layerCount': {'python_name': ['layer', 'count']},
    }
}
