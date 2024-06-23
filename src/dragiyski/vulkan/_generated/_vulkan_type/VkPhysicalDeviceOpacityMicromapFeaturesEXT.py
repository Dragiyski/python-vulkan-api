import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('micromap', ctypes.c_uint32),
        ('micromapCaptureReplay', ctypes.c_uint32),
        ('micromapHostCommands', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkDeviceCreateInfo',
        'VkPhysicalDeviceFeatures2',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_OPACITY_MICROMAP_FEATURES_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'micromap': {'python_name': ['micromap']},
        'micromapCaptureReplay': {'python_name': ['micromap', 'capture', 'replay']},
        'micromapHostCommands': {'python_name': ['micromap', 'host', 'commands']},
    }
}
