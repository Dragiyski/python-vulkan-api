import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('deviceUUID', ctypes.ARRAY(ctypes.c_uint8, 16)),
        ('driverUUID', ctypes.ARRAY(ctypes.c_uint8, 16)),
        ('deviceLUID', ctypes.ARRAY(ctypes.c_uint8, 8)),
        ('deviceNodeMask', ctypes.c_uint32),
        ('deviceLUIDValid', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_ID_PROPERTIES', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'deviceUUID': {'python_name': ['device', 'uuid']},
        'driverUUID': {'python_name': ['driver', 'uuid']},
        'deviceLUID': {'python_name': ['device', 'luid']},
        'deviceNodeMask': {'python_name': ['device', 'node', 'mask']},
        'deviceLUIDValid': {'python_name': ['device', 'luidvalid']},
    }
}
