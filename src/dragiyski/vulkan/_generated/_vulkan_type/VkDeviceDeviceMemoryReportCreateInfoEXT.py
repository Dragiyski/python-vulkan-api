import ctypes

class CType(ctypes.Structure):
    pass

from ..vulkan_callback import vkDeviceMemoryReportCallbackEXT

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('pfnUserCallback', vkDeviceMemoryReportCallbackEXT),
    ('pUserData', ctypes.c_void_p),
]

descriptor = {
    'extends': {
        'VkDeviceCreateInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DEVICE_DEVICE_MEMORY_REPORT_CREATE_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkDeviceMemoryReportFlagsEXT'},
        'pfnUserCallback': {'python_name': ['pfn', 'user', 'callback']},
        'pUserData': {'python_name': ['p', 'user', 'data']},
    }
}
