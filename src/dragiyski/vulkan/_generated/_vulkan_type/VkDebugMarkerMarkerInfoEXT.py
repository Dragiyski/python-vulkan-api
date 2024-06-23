import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pMarkerName', ctypes.c_char_p),
        ('color', ctypes.ARRAY(ctypes.c_float, 4)),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkCmdDebugMarkerBeginEXT',
        'vkCmdDebugMarkerInsertEXT',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DEBUG_MARKER_MARKER_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'pMarkerName': {'python_name': ['p', 'marker', 'name'], 'len': [['null-terminated']]},
        'color': {'python_name': ['color']},
    }
}
