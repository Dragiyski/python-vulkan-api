import ctypes

class CType(ctypes.Structure):
    pass

from ..vulkan_callback import vkDebugUtilsMessengerCallbackEXT

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('messageSeverity', ctypes.c_uint32),
    ('messageType', ctypes.c_uint32),
    ('pfnUserCallback', vkDebugUtilsMessengerCallbackEXT),
    ('pUserData', ctypes.c_void_p),
]

descriptor = {
    'extends': {
        'VkInstanceCreateInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkCreateDebugUtilsMessengerEXT',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DEBUG_UTILS_MESSENGER_CREATE_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkDebugUtilsMessengerCreateFlagsEXT'},
        'messageSeverity': {'python_name': ['message', 'severity'], 'type': 'VkDebugUtilsMessageSeverityFlagsEXT'},
        'messageType': {'python_name': ['message', 'type'], 'type': 'VkDebugUtilsMessageTypeFlagsEXT'},
        'pfnUserCallback': {'python_name': ['pfn', 'user', 'callback']},
        'pUserData': {'python_name': ['p', 'user', 'data']},
    }
}
