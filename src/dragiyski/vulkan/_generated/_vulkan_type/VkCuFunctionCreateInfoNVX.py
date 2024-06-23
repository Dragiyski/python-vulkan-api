import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('module', ctypes.c_void_p),
        ('pName', ctypes.c_char_p),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkCreateCuFunctionNVX',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_CU_FUNCTION_CREATE_INFO_NVX', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'module': {'python_name': ['module']},
        'pName': {'python_name': ['p', 'name'], 'len': [['null-terminated']]},
    }
}
