import ctypes

class CType(ctypes.Structure):
    pass

from ..vulkan_callback import vkDebugReportCallbackEXT

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('pfnCallback', vkDebugReportCallbackEXT),
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
        'vkCreateDebugReportCallbackEXT',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DEBUG_REPORT_CALLBACK_CREATE_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkDebugReportFlagsEXT'},
        'pfnCallback': {'python_name': ['pfn', 'callback']},
        'pUserData': {'python_name': ['p', 'user', 'data']},
    }
}
