import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('extensionName', ctypes.ARRAY(ctypes.c_char, 256)),
        ('specVersion', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkVideoCapabilitiesKHR',
        'VkVideoSessionCreateInfoKHR',
    },
    'input_of': set(),
    'output_of': {
        'vkEnumerateDeviceExtensionProperties',
        'vkEnumerateInstanceExtensionProperties',
    },
    'member_map': {
        'extensionName': {'python_name': ['extension', 'name'], 'len': [['null-terminated']]},
        'specVersion': {'python_name': ['spec', 'version']},
    }
}
