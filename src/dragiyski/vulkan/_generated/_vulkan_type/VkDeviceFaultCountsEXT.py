import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('addressInfoCount', ctypes.c_uint32),
        ('vendorInfoCount', ctypes.c_uint32),
        ('vendorBinarySize', ctypes.c_uint64),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetDeviceFaultInfoEXT',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DEVICE_FAULT_COUNTS_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'addressInfoCount': {'python_name': ['address', 'info', 'count']},
        'vendorInfoCount': {'python_name': ['vendor', 'info', 'count']},
        'vendorBinarySize': {'python_name': ['vendor', 'binary', 'size']},
    }
}
