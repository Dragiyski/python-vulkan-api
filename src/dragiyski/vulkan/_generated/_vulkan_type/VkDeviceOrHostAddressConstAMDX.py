import ctypes

class CType(ctypes.Union):
    _fields_ = [
        ('deviceAddress', ctypes.c_uint64),
        ('hostAddress', ctypes.c_void_p),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkDispatchGraphCountInfoAMDX',
        'VkDispatchGraphInfoAMDX',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'deviceAddress': {'python_name': ['device', 'address']},
        'hostAddress': {'python_name': ['host', 'address']},
    }
}
