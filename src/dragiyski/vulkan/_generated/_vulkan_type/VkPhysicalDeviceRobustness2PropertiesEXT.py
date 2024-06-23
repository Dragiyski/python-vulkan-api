import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('robustStorageBufferAccessSizeAlignment', ctypes.c_uint64),
        ('robustUniformBufferAccessSizeAlignment', ctypes.c_uint64),
    ]

descriptor = {
    'extends': {
        'VkPhysicalDeviceProperties2',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_ROBUSTNESS_2_PROPERTIES_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'robustStorageBufferAccessSizeAlignment': {'python_name': ['robust', 'storage', 'buffer', 'access', 'size', 'alignment']},
        'robustUniformBufferAccessSizeAlignment': {'python_name': ['robust', 'uniform', 'buffer', 'access', 'size', 'alignment']},
    }
}
