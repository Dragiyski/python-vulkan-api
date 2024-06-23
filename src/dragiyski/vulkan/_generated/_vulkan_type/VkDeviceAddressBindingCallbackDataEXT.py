import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('baseAddress', ctypes.c_uint64),
        ('size', ctypes.c_uint64),
        ('bindingType', ctypes.c_int),
    ]

descriptor = {
    'extends': {
        'VkDebugUtilsMessengerCallbackDataEXT',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DEVICE_ADDRESS_BINDING_CALLBACK_DATA_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkDeviceAddressBindingFlagsEXT'},
        'baseAddress': {'python_name': ['base', 'address']},
        'size': {'python_name': ['size']},
        'bindingType': {'python_name': ['binding', 'type'], 'type': 'VkDeviceAddressBindingTypeEXT'},
    }
}
