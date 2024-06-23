import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('perViewPositionAllComponents', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MULTIVIEW_PER_VIEW_ATTRIBUTES_PROPERTIES_NVX', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'perViewPositionAllComponents': {'python_name': ['per', 'view', 'position', 'all', 'components']},
    }
}
