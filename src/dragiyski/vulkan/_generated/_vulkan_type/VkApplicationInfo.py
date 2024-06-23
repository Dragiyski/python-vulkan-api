import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pApplicationName', ctypes.c_char_p),
        ('applicationVersion', ctypes.c_uint32),
        ('pEngineName', ctypes.c_char_p),
        ('engineVersion', ctypes.c_uint32),
        ('apiVersion', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkApplicationParametersEXT',
    },
    'includes': set(),
    'included_in': {
        'VkInstanceCreateInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_APPLICATION_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'pApplicationName': {'python_name': ['p', 'application', 'name'], 'len': [['null-terminated']]},
        'applicationVersion': {'python_name': ['application', 'version']},
        'pEngineName': {'python_name': ['p', 'engine', 'name'], 'len': [['null-terminated']]},
        'engineVersion': {'python_name': ['engine', 'version']},
        'apiVersion': {'python_name': ['api', 'version']},
    }
}
