import ctypes

class CType(ctypes.Structure):
    pass

from .VkComponentMapping import CType as VkComponentMapping

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('format', ctypes.c_int),
    ('componentMapping', VkComponentMapping),
    ('imageCreateFlags', ctypes.c_uint32),
    ('imageType', ctypes.c_int),
    ('imageTiling', ctypes.c_int),
    ('imageUsageFlags', ctypes.c_uint32),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkComponentMapping',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetPhysicalDeviceVideoFormatPropertiesKHR',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VIDEO_FORMAT_PROPERTIES_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'format': {'python_name': ['format'], 'type': 'VkFormat'},
        'componentMapping': {'python_name': ['component', 'mapping'], 'type': 'VkComponentMapping'},
        'imageCreateFlags': {'python_name': ['image', 'create', 'flags'], 'type': 'VkImageCreateFlags'},
        'imageType': {'python_name': ['image', 'type'], 'type': 'VkImageType'},
        'imageTiling': {'python_name': ['image', 'tiling'], 'type': 'VkImageTiling'},
        'imageUsageFlags': {'python_name': ['image', 'usage', 'flags'], 'type': 'VkImageUsageFlags'},
    }
}
