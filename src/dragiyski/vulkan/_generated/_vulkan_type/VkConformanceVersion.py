import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('major', ctypes.c_uint8),
        ('minor', ctypes.c_uint8),
        ('subminor', ctypes.c_uint8),
        ('patch', ctypes.c_uint8),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkPhysicalDeviceDriverProperties',
        'VkPhysicalDeviceVulkan12Properties',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'major': {'python_name': ['major']},
        'minor': {'python_name': ['minor']},
        'subminor': {'python_name': ['subminor']},
        'patch': {'python_name': ['patch']},
    }
}
