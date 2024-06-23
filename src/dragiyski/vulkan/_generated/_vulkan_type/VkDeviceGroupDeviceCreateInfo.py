import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('physicalDeviceCount', ctypes.c_uint32),
        ('pPhysicalDevices', ctypes.POINTER(ctypes.c_void_p)),
    ]

descriptor = {
    'extends': {
        'VkDeviceCreateInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DEVICE_GROUP_DEVICE_CREATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'physicalDeviceCount': {'python_name': ['physical', 'device', 'count']},
        'pPhysicalDevices': {'python_name': ['p', 'physical', 'devices'], 'len': [['physicalDeviceCount']]},
    }
}
