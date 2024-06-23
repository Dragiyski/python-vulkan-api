import ctypes

class CType(ctypes.Structure):
    pass

from .VkSubresourceLayout import CType as VkSubresourceLayout

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('subresourceLayout', VkSubresourceLayout),
]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkImageCompressionPropertiesEXT',
        'VkSubresourceHostMemcpySizeEXT',
    },
    'includes': {
        'VkSubresourceLayout',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetDeviceImageSubresourceLayoutKHR',
        'vkGetImageSubresourceLayout2KHR',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_SUBRESOURCE_LAYOUT_2_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'subresourceLayout': {'python_name': ['subresource', 'layout'], 'type': 'VkSubresourceLayout'},
    }
}
