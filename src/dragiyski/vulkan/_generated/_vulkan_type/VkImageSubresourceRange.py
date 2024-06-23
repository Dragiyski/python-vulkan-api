import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('aspectMask', ctypes.c_uint32),
        ('baseMipLevel', ctypes.c_uint32),
        ('levelCount', ctypes.c_uint32),
        ('baseArrayLayer', ctypes.c_uint32),
        ('layerCount', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkHostImageLayoutTransitionInfoEXT',
        'VkImageMemoryBarrier',
        'VkImageMemoryBarrier2',
        'VkImageViewCreateInfo',
    },
    'input_of': {
        'vkCmdClearColorImage',
        'vkCmdClearDepthStencilImage',
    },
    'output_of': set(),
    'member_map': {
        'aspectMask': {'python_name': ['aspect', 'mask'], 'type': 'VkImageAspectFlags'},
        'baseMipLevel': {'python_name': ['base', 'mip', 'level']},
        'levelCount': {'python_name': ['level', 'count']},
        'baseArrayLayer': {'python_name': ['base', 'array', 'layer']},
        'layerCount': {'python_name': ['layer', 'count']},
    }
}
