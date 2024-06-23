import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('ycbcr2plane444Formats', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_YCBCR_2_PLANE_444_FORMATS_FEATURES_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'ycbcr2plane444Formats': {'python_name': ['ycbcr2plane444', 'formats']},
    }
}
