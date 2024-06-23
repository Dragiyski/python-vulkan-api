import ctypes

class CType(ctypes.Structure):
    pass

from .VkMemoryRequirements import CType as VkMemoryRequirements

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('memoryRequirements', VkMemoryRequirements),
]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkMemoryDedicatedRequirements',
    },
    'includes': {
        'VkMemoryRequirements',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetAccelerationStructureMemoryRequirementsNV',
        'vkGetBufferMemoryRequirements2',
        'vkGetDeviceBufferMemoryRequirements',
        'vkGetDeviceImageMemoryRequirements',
        'vkGetGeneratedCommandsMemoryRequirementsNV',
        'vkGetImageMemoryRequirements2',
        'vkGetPipelineIndirectMemoryRequirementsNV',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_MEMORY_REQUIREMENTS_2', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'memoryRequirements': {'python_name': ['memory', 'requirements'], 'type': 'VkMemoryRequirements'},
    }
}
