import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('disabledValidationCheckCount', ctypes.c_uint32),
        ('pDisabledValidationChecks', ctypes.POINTER(ctypes.c_int)),
    ]

descriptor = {
    'extends': {
        'VkInstanceCreateInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VALIDATION_FLAGS_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'disabledValidationCheckCount': {'python_name': ['disabled', 'validation', 'check', 'count']},
        'pDisabledValidationChecks': {'python_name': ['p', 'disabled', 'validation', 'checks'], 'len': [['disabledValidationCheckCount']], 'type': 'VkValidationCheckEXT'},
    }
}
