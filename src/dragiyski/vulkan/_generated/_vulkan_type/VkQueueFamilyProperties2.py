import ctypes

class CType(ctypes.Structure):
    pass

from .VkQueueFamilyProperties import CType as VkQueueFamilyProperties

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('queueFamilyProperties', VkQueueFamilyProperties),
]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkQueueFamilyCheckpointProperties2NV',
        'VkQueueFamilyCheckpointPropertiesNV',
        'VkQueueFamilyGlobalPriorityPropertiesKHR',
        'VkQueueFamilyQueryResultStatusPropertiesKHR',
        'VkQueueFamilyVideoPropertiesKHR',
    },
    'includes': {
        'VkQueueFamilyProperties',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetPhysicalDeviceQueueFamilyProperties2',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_QUEUE_FAMILY_PROPERTIES_2', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'queueFamilyProperties': {'python_name': ['queue', 'family', 'properties'], 'type': 'VkQueueFamilyProperties'},
    }
}
