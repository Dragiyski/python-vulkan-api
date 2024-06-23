import ctypes

class CType(ctypes.Structure):
    pass

from .VkApplicationInfo import CType as VkApplicationInfo

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('pApplicationInfo', ctypes.POINTER(VkApplicationInfo)),
    ('enabledLayerCount', ctypes.c_uint32),
    ('ppEnabledLayerNames', ctypes.POINTER(ctypes.c_char_p)),
    ('enabledExtensionCount', ctypes.c_uint32),
    ('ppEnabledExtensionNames', ctypes.POINTER(ctypes.c_char_p)),
]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkDebugReportCallbackCreateInfoEXT',
        'VkDebugUtilsMessengerCreateInfoEXT',
        'VkDirectDriverLoadingListLUNARG',
        'VkExportMetalObjectCreateInfoEXT',
        'VkLayerSettingsCreateInfoEXT',
        'VkValidationFeaturesEXT',
        'VkValidationFlagsEXT',
    },
    'includes': {
        'VkApplicationInfo',
    },
    'included_in': set(),
    'input_of': {
        'vkCreateInstance',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_INSTANCE_CREATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkInstanceCreateFlags'},
        'pApplicationInfo': {'python_name': ['p', 'application', 'info'], 'type': 'VkApplicationInfo'},
        'enabledLayerCount': {'python_name': ['enabled', 'layer', 'count']},
        'ppEnabledLayerNames': {'python_name': ['pp', 'enabled', 'layer', 'names'], 'len': [['enabledLayerCount'], ['null-terminated']]},
        'enabledExtensionCount': {'python_name': ['enabled', 'extension', 'count']},
        'ppEnabledExtensionNames': {'python_name': ['pp', 'enabled', 'extension', 'names'], 'len': [['enabledExtensionCount'], ['null-terminated']]},
    }
}
