import ctypes

class CType(ctypes.Structure):
    pass

from .VkImageCreateInfo import CType as VkImageCreateInfo
from .VkImageSubresource2KHR import CType as VkImageSubresource2KHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pCreateInfo', ctypes.POINTER(VkImageCreateInfo)),
    ('pSubresource', ctypes.POINTER(VkImageSubresource2KHR)),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkImageCreateInfo',
        'VkImageSubresource2KHR',
    },
    'included_in': set(),
    'input_of': {
        'vkGetDeviceImageSubresourceLayoutKHR',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DEVICE_IMAGE_SUBRESOURCE_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'pCreateInfo': {'python_name': ['p', 'create', 'info'], 'type': 'VkImageCreateInfo'},
        'pSubresource': {'python_name': ['p', 'subresource'], 'type': 'VkImageSubresource2KHR'},
    }
}
