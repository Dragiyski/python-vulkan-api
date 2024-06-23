import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('localDimmingSupport', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkSurfaceCapabilities2KHR',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DISPLAY_NATIVE_HDR_SURFACE_CAPABILITIES_AMD', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'localDimmingSupport': {'python_name': ['local', 'dimming', 'support']},
    }
}
