import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('filterMinmaxSingleComponentFormats', ctypes.c_uint32),
        ('filterMinmaxImageComponentMapping', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SAMPLER_FILTER_MINMAX_PROPERTIES', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'filterMinmaxSingleComponentFormats': {'python_name': ['filter', 'minmax', 'single', 'component', 'formats']},
        'filterMinmaxImageComponentMapping': {'python_name': ['filter', 'minmax', 'image', 'component', 'mapping']},
    }
}
