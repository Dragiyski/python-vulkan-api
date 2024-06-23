import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('format', ctypes.c_int),
        ('colorSpace', ctypes.c_int),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkSurfaceFormat2KHR',
    },
    'input_of': set(),
    'output_of': {
        'vkGetPhysicalDeviceSurfaceFormatsKHR',
    },
    'member_map': {
        'format': {'python_name': ['format'], 'type': 'VkFormat'},
        'colorSpace': {'python_name': ['color', 'space'], 'type': 'VkColorSpaceKHR'},
    }
}
