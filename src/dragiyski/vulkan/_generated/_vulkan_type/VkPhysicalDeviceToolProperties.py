import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('name', ctypes.ARRAY(ctypes.c_char, 256)),
        ('version', ctypes.ARRAY(ctypes.c_char, 256)),
        ('purposes', ctypes.c_uint32),
        ('description', ctypes.ARRAY(ctypes.c_char, 256)),
        ('layer', ctypes.ARRAY(ctypes.c_char, 256)),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetPhysicalDeviceToolProperties',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TOOL_PROPERTIES', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'name': {'python_name': ['name'], 'len': [['null-terminated']]},
        'version': {'python_name': ['version'], 'len': [['null-terminated']]},
        'purposes': {'python_name': ['purposes'], 'type': 'VkToolPurposeFlags'},
        'description': {'python_name': ['description'], 'len': [['null-terminated']]},
        'layer': {'python_name': ['layer'], 'len': [['null-terminated']]},
    }
}
