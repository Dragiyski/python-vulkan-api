import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('descriptorBuffer', ctypes.c_uint32),
        ('descriptorBufferCaptureReplay', ctypes.c_uint32),
        ('descriptorBufferImageLayoutIgnored', ctypes.c_uint32),
        ('descriptorBufferPushDescriptors', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DESCRIPTOR_BUFFER_FEATURES_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'descriptorBuffer': {'python_name': ['descriptor', 'buffer']},
        'descriptorBufferCaptureReplay': {'python_name': ['descriptor', 'buffer', 'capture', 'replay']},
        'descriptorBufferImageLayoutIgnored': {'python_name': ['descriptor', 'buffer', 'image', 'layout', 'ignored']},
        'descriptorBufferPushDescriptors': {'python_name': ['descriptor', 'buffer', 'push', 'descriptors']},
    }
}
