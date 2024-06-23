import ctypes

class CType(ctypes.Structure):
    pass

from .VkImageCreateInfo import CType as VkImageCreateInfo

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pCreateInfo', ctypes.POINTER(VkImageCreateInfo)),
    ('planeAspect', ctypes.c_uint32),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkImageCreateInfo',
    },
    'included_in': set(),
    'input_of': {
        'vkGetDeviceImageMemoryRequirements',
        'vkGetDeviceImageSparseMemoryRequirements',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DEVICE_IMAGE_MEMORY_REQUIREMENTS', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'pCreateInfo': {'python_name': ['p', 'create', 'info'], 'type': 'VkImageCreateInfo'},
        'planeAspect': {'python_name': ['plane', 'aspect'], 'type': 'VkImageAspectFlagBits'},
    }
}
