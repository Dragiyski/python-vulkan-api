import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('rectangularLines', ctypes.c_uint32),
        ('bresenhamLines', ctypes.c_uint32),
        ('smoothLines', ctypes.c_uint32),
        ('stippledRectangularLines', ctypes.c_uint32),
        ('stippledBresenhamLines', ctypes.c_uint32),
        ('stippledSmoothLines', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_LINE_RASTERIZATION_FEATURES_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'rectangularLines': {'python_name': ['rectangular', 'lines']},
        'bresenhamLines': {'python_name': ['bresenham', 'lines']},
        'smoothLines': {'python_name': ['smooth', 'lines']},
        'stippledRectangularLines': {'python_name': ['stippled', 'rectangular', 'lines']},
        'stippledBresenhamLines': {'python_name': ['stippled', 'bresenham', 'lines']},
        'stippledSmoothLines': {'python_name': ['stippled', 'smooth', 'lines']},
    }
}
