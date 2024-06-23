import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pixelRate', ctypes.c_uint32),
        ('texelRate', ctypes.c_uint32),
        ('fmaRate', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_CORE_PROPERTIES_ARM', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'pixelRate': {'python_name': ['pixel', 'rate']},
        'texelRate': {'python_name': ['texel', 'rate']},
        'fmaRate': {'python_name': ['fma', 'rate']},
    }
}
