import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxOpacity2StateSubdivisionLevel', ctypes.c_uint32),
        ('maxOpacity4StateSubdivisionLevel', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_OPACITY_MICROMAP_PROPERTIES_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'maxOpacity2StateSubdivisionLevel': {'python_name': ['max', 'opacity2', 'state', 'subdivision', 'level']},
        'maxOpacity4StateSubdivisionLevel': {'python_name': ['max', 'opacity4', 'state', 'subdivision', 'level']},
    }
}
