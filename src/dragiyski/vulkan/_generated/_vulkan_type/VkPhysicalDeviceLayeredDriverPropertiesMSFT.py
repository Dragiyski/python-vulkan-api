import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('underlyingAPI', ctypes.c_int),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_LAYERED_DRIVER_PROPERTIES_MSFT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'underlyingAPI': {'python_name': ['underlying', 'api'], 'type': 'VkLayeredDriverUnderlyingApiMSFT'},
    }
}
