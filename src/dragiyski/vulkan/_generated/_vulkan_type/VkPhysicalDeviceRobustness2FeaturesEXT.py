import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('robustBufferAccess2', ctypes.c_uint32),
        ('robustImageAccess2', ctypes.c_uint32),
        ('nullDescriptor', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_ROBUSTNESS_2_FEATURES_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'robustBufferAccess2': {'python_name': ['robust', 'buffer', 'access2']},
        'robustImageAccess2': {'python_name': ['robust', 'image', 'access2']},
        'nullDescriptor': {'python_name': ['null', 'descriptor']},
    }
}
