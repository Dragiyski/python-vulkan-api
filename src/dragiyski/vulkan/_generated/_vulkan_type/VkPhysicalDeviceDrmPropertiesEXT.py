import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('hasPrimary', ctypes.c_uint32),
        ('hasRender', ctypes.c_uint32),
        ('primaryMajor', ctypes.c_int64),
        ('primaryMinor', ctypes.c_int64),
        ('renderMajor', ctypes.c_int64),
        ('renderMinor', ctypes.c_int64),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DRM_PROPERTIES_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'hasPrimary': {'python_name': ['has', 'primary']},
        'hasRender': {'python_name': ['has', 'render']},
        'primaryMajor': {'python_name': ['primary', 'major']},
        'primaryMinor': {'python_name': ['primary', 'minor']},
        'renderMajor': {'python_name': ['render', 'major']},
        'renderMinor': {'python_name': ['render', 'minor']},
    }
}
