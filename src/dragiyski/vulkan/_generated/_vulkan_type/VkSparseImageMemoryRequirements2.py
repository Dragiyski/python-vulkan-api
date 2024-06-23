import ctypes

class CType(ctypes.Structure):
    pass

from .VkSparseImageMemoryRequirements import CType as VkSparseImageMemoryRequirements

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('memoryRequirements', VkSparseImageMemoryRequirements),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkSparseImageMemoryRequirements',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetDeviceImageSparseMemoryRequirements',
        'vkGetImageSparseMemoryRequirements2',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_SPARSE_IMAGE_MEMORY_REQUIREMENTS_2', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'memoryRequirements': {'python_name': ['memory', 'requirements'], 'type': 'VkSparseImageMemoryRequirements'},
    }
}
