import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('prefersDedicatedAllocation', ctypes.c_uint32),
        ('requiresDedicatedAllocation', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkMemoryRequirements2',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_MEMORY_DEDICATED_REQUIREMENTS', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'prefersDedicatedAllocation': {'python_name': ['prefers', 'dedicated', 'allocation']},
        'requiresDedicatedAllocation': {'python_name': ['requires', 'dedicated', 'allocation']},
    }
}
