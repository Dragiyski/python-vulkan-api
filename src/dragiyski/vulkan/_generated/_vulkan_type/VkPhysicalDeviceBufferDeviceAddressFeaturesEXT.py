import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('bufferDeviceAddress', ctypes.c_uint32),
        ('bufferDeviceAddressCaptureReplay', ctypes.c_uint32),
        ('bufferDeviceAddressMultiDevice', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkDeviceCreateInfo',
        'VkPhysicalDeviceFeatures2',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_BUFFER_DEVICE_ADDRESS_FEATURES_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'bufferDeviceAddress': {'python_name': ['buffer', 'device', 'address']},
        'bufferDeviceAddressCaptureReplay': {'python_name': ['buffer', 'device', 'address', 'capture', 'replay']},
        'bufferDeviceAddressMultiDevice': {'python_name': ['buffer', 'device', 'address', 'multi', 'device']},
    }
}
