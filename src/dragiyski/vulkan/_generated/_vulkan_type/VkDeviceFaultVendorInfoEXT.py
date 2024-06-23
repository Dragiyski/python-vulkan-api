import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('description', ctypes.ARRAY(ctypes.c_char, 256)),
        ('vendorFaultCode', ctypes.c_uint64),
        ('vendorFaultData', ctypes.c_uint64),
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
        'description': {'python_name': ['description'], 'len': [['null-terminated']]},
        'vendorFaultCode': {'python_name': ['vendor', 'fault', 'code']},
        'vendorFaultData': {'python_name': ['vendor', 'fault', 'data']},
    }
}
