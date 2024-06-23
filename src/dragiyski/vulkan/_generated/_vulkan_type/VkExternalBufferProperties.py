import ctypes

class CType(ctypes.Structure):
    pass

from .VkExternalMemoryProperties import CType as VkExternalMemoryProperties

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('externalMemoryProperties', VkExternalMemoryProperties),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkExternalMemoryProperties',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetPhysicalDeviceExternalBufferProperties',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_EXTERNAL_BUFFER_PROPERTIES', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'externalMemoryProperties': {'python_name': ['external', 'memory', 'properties'], 'type': 'VkExternalMemoryProperties'},
    }
}
