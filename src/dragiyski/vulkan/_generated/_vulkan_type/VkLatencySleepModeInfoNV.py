import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('lowLatencyMode', ctypes.c_uint32),
        ('lowLatencyBoost', ctypes.c_uint32),
        ('minimumIntervalUs', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkSetLatencySleepModeNV',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_LATENCY_SLEEP_MODE_INFO_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'lowLatencyMode': {'python_name': ['low', 'latency', 'mode']},
        'lowLatencyBoost': {'python_name': ['low', 'latency', 'boost']},
        'minimumIntervalUs': {'python_name': ['minimum', 'interval', 'us']},
    }
}
