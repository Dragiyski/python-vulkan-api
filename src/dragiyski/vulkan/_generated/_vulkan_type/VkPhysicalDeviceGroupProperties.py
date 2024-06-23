import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('physicalDeviceCount', ctypes.c_uint32),
        ('physicalDevices', ctypes.ARRAY(ctypes.c_void_p, 32)),
        ('subsetAllocation', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkEnumeratePhysicalDeviceGroups',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_GROUP_PROPERTIES', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'physicalDeviceCount': {'python_name': ['physical', 'device', 'count']},
        'physicalDevices': {'python_name': ['physical', 'devices'], 'len': [['physicalDeviceCount']]},
        'subsetAllocation': {'python_name': ['subset', 'allocation']},
    }
}
