import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxMultiviewViewCount', ctypes.c_uint32),
        ('maxMultiviewInstanceIndex', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MULTIVIEW_PROPERTIES', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'maxMultiviewViewCount': {'python_name': ['max', 'multiview', 'view', 'count']},
        'maxMultiviewInstanceIndex': {'python_name': ['max', 'multiview', 'instance', 'index']},
    }
}
