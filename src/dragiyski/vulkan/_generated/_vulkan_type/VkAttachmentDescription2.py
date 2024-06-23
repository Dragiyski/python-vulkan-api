import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('format', ctypes.c_int),
        ('samples', ctypes.c_uint32),
        ('loadOp', ctypes.c_int),
        ('storeOp', ctypes.c_int),
        ('stencilLoadOp', ctypes.c_int),
        ('stencilStoreOp', ctypes.c_int),
        ('initialLayout', ctypes.c_int),
        ('finalLayout', ctypes.c_int),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkAttachmentDescriptionStencilLayout',
        'VkExternalFormatANDROID',
    },
    'includes': set(),
    'included_in': {
        'VkRenderPassCreateInfo2',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_ATTACHMENT_DESCRIPTION_2', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkAttachmentDescriptionFlags'},
        'format': {'python_name': ['format'], 'type': 'VkFormat'},
        'samples': {'python_name': ['samples'], 'type': 'VkSampleCountFlagBits'},
        'loadOp': {'python_name': ['load', 'op'], 'type': 'VkAttachmentLoadOp'},
        'storeOp': {'python_name': ['store', 'op'], 'type': 'VkAttachmentStoreOp'},
        'stencilLoadOp': {'python_name': ['stencil', 'load', 'op'], 'type': 'VkAttachmentLoadOp'},
        'stencilStoreOp': {'python_name': ['stencil', 'store', 'op'], 'type': 'VkAttachmentStoreOp'},
        'initialLayout': {'python_name': ['initial', 'layout'], 'type': 'VkImageLayout'},
        'finalLayout': {'python_name': ['final', 'layout'], 'type': 'VkImageLayout'},
    }
}
