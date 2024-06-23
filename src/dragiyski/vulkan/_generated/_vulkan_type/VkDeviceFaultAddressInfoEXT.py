import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('addressType', ctypes.c_int),
        ('reportedAddress', ctypes.c_uint64),
        ('addressPrecision', ctypes.c_uint64),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkDeviceFaultInfoEXT',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'addressType': {'python_name': ['address', 'type'], 'type': 'VkDeviceFaultAddressTypeEXT'},
        'reportedAddress': {'python_name': ['reported', 'address']},
        'addressPrecision': {'python_name': ['address', 'precision']},
    }
}
