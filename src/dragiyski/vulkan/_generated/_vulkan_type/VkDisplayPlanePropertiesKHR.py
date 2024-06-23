import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('currentDisplay', ctypes.c_void_p),
        ('currentStackIndex', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkDisplayPlaneProperties2KHR',
    },
    'input_of': set(),
    'output_of': {
        'vkGetPhysicalDeviceDisplayPlanePropertiesKHR',
    },
    'member_map': {
        'currentDisplay': {'python_name': ['current', 'display']},
        'currentStackIndex': {'python_name': ['current', 'stack', 'index']},
    }
}
