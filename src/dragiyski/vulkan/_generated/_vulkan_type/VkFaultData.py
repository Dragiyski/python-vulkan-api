import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('faultLevel', ctypes.c_int),
        ('faultType', ctypes.c_int),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkFaultCallbackInfo',
    },
    'input_of': set(),
    'output_of': {
        'vkGetFaultData',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_FAULT_DATA', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'faultLevel': {'python_name': ['fault', 'level'], 'type': 'VkFaultLevel'},
        'faultType': {'python_name': ['fault', 'type'], 'type': 'VkFaultType'},
    }
}
