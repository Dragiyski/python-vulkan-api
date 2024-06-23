import ctypes

class CType(ctypes.Structure):
    pass

from .VkMemoryRequirements import CType as VkMemoryRequirements

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('memoryBindIndex', ctypes.c_uint32),
    ('memoryRequirements', VkMemoryRequirements),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkMemoryRequirements',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetVideoSessionMemoryRequirementsKHR',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VIDEO_SESSION_MEMORY_REQUIREMENTS_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'memoryBindIndex': {'python_name': ['memory', 'bind', 'index']},
        'memoryRequirements': {'python_name': ['memory', 'requirements'], 'type': 'VkMemoryRequirements'},
    }
}
