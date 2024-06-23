import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('sciBufImport', ctypes.c_uint32),
        ('sciBufExport', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTERNAL_MEMORY_SCI_BUF_FEATURES_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'sciBufImport': {'python_name': ['sci', 'buf', 'import']},
        'sciBufExport': {'python_name': ['sci', 'buf', 'export']},
    }
}
