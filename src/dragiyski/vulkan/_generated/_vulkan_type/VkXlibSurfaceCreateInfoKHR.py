import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('dpy', ctypes.c_void_p),
        ('window', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkCreateXlibSurfaceKHR',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_XLIB_SURFACE_CREATE_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkXlibSurfaceCreateFlagsKHR'},
        'dpy': {'python_name': ['dpy']},
        'window': {'python_name': ['window']},
    }
}
