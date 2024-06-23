import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('usage', ctypes.c_uint32),
        ('width', ctypes.c_uint32),
        ('height', ctypes.c_uint32),
        ('layerCount', ctypes.c_uint32),
        ('viewFormatCount', ctypes.c_uint32),
        ('pViewFormats', ctypes.POINTER(ctypes.c_int)),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkFramebufferAttachmentsCreateInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_FRAMEBUFFER_ATTACHMENT_IMAGE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkImageCreateFlags'},
        'usage': {'python_name': ['usage'], 'type': 'VkImageUsageFlags'},
        'width': {'python_name': ['width']},
        'height': {'python_name': ['height']},
        'layerCount': {'python_name': ['layer', 'count']},
        'viewFormatCount': {'python_name': ['view', 'format', 'count']},
        'pViewFormats': {'python_name': ['p', 'view', 'formats'], 'len': [['viewFormatCount']], 'type': 'VkFormat'},
    }
}
