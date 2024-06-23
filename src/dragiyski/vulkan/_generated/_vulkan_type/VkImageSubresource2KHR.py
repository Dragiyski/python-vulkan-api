import ctypes

class CType(ctypes.Structure):
    pass

from .VkImageSubresource import CType as VkImageSubresource

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('imageSubresource', VkImageSubresource),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkImageSubresource',
    },
    'included_in': {
        'VkDeviceImageSubresourceInfoKHR',
    },
    'input_of': {
        'vkGetImageSubresourceLayout2KHR',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_IMAGE_SUBRESOURCE_2_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'imageSubresource': {'python_name': ['image', 'subresource'], 'type': 'VkImageSubresource'},
    }
}
