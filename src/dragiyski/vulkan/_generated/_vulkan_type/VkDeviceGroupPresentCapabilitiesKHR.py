import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('presentMask', ctypes.ARRAY(ctypes.c_uint32, 32)),
        ('modes', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetDeviceGroupPresentCapabilitiesKHR',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DEVICE_GROUP_PRESENT_CAPABILITIES_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'presentMask': {'python_name': ['present', 'mask']},
        'modes': {'python_name': ['modes'], 'type': 'VkDeviceGroupPresentModeFlagsKHR'},
    }
}
