import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('workgroupMemoryExplicitLayout', ctypes.c_uint32),
        ('workgroupMemoryExplicitLayoutScalarBlockLayout', ctypes.c_uint32),
        ('workgroupMemoryExplicitLayout8BitAccess', ctypes.c_uint32),
        ('workgroupMemoryExplicitLayout16BitAccess', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_WORKGROUP_MEMORY_EXPLICIT_LAYOUT_FEATURES_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'workgroupMemoryExplicitLayout': {'python_name': ['workgroup', 'memory', 'explicit', 'layout']},
        'workgroupMemoryExplicitLayoutScalarBlockLayout': {'python_name': ['workgroup', 'memory', 'explicit', 'layout', 'scalar', 'block', 'layout']},
        'workgroupMemoryExplicitLayout8BitAccess': {'python_name': ['workgroup', 'memory', 'explicit', 'layout8', 'bit', 'access']},
        'workgroupMemoryExplicitLayout16BitAccess': {'python_name': ['workgroup', 'memory', 'explicit', 'layout16', 'bit', 'access']},
    }
}
