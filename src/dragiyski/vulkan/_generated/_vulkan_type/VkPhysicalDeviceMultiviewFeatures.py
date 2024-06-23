import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('multiview', ctypes.c_uint32),
        ('multiviewGeometryShader', ctypes.c_uint32),
        ('multiviewTessellationShader', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkDeviceCreateInfo',
        'VkPhysicalDeviceFeatures2',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MULTIVIEW_FEATURES', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'multiview': {'python_name': ['multiview']},
        'multiviewGeometryShader': {'python_name': ['multiview', 'geometry', 'shader']},
        'multiviewTessellationShader': {'python_name': ['multiview', 'tessellation', 'shader']},
    }
}
