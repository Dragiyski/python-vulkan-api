import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('filterCubic', ctypes.c_uint32),
        ('filterCubicMinmax', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkImageFormatProperties2',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_FILTER_CUBIC_IMAGE_VIEW_IMAGE_FORMAT_PROPERTIES_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'filterCubic': {'python_name': ['filter', 'cubic']},
        'filterCubicMinmax': {'python_name': ['filter', 'cubic', 'minmax']},
    }
}
