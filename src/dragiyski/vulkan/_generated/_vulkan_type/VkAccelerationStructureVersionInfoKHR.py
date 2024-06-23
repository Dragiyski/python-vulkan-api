import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pVersionData', ctypes.POINTER(ctypes.c_uint8)),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkGetDeviceAccelerationStructureCompatibilityKHR',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_VERSION_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'pVersionData': {'python_name': ['p', 'version', 'data'], 'len': [['latexmath:[2 \\times \\mathtt{VK\\_UUID\\_SIZE}]']]},
    }
}
