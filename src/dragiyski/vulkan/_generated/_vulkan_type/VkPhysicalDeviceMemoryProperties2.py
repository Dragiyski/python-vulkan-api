import ctypes

class CType(ctypes.Structure):
    pass

from .VkPhysicalDeviceMemoryProperties import CType as VkPhysicalDeviceMemoryProperties

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('memoryProperties', VkPhysicalDeviceMemoryProperties),
]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkPhysicalDeviceMemoryBudgetPropertiesEXT',
    },
    'includes': {
        'VkPhysicalDeviceMemoryProperties',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetPhysicalDeviceMemoryProperties2',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MEMORY_PROPERTIES_2', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'memoryProperties': {'python_name': ['memory', 'properties'], 'type': 'VkPhysicalDeviceMemoryProperties'},
    }
}
