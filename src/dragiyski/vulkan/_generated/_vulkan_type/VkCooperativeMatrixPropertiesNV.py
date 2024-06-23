import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('MSize', ctypes.c_uint32),
        ('NSize', ctypes.c_uint32),
        ('KSize', ctypes.c_uint32),
        ('AType', ctypes.c_int),
        ('BType', ctypes.c_int),
        ('CType', ctypes.c_int),
        ('DType', ctypes.c_int),
        ('scope', ctypes.c_int),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetPhysicalDeviceCooperativeMatrixPropertiesNV',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_COOPERATIVE_MATRIX_PROPERTIES_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'MSize': {'python_name': ['msize']},
        'NSize': {'python_name': ['nsize']},
        'KSize': {'python_name': ['ksize']},
        'AType': {'python_name': ['atype'], 'type': 'VkComponentTypeKHR'},
        'BType': {'python_name': ['btype'], 'type': 'VkComponentTypeKHR'},
        'CType': {'python_name': ['ctype'], 'type': 'VkComponentTypeKHR'},
        'DType': {'python_name': ['dtype'], 'type': 'VkComponentTypeKHR'},
        'scope': {'python_name': ['scope'], 'type': 'VkScopeKHR'},
    }
}
