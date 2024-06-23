import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('presentModeCount', ctypes.c_uint32),
        ('pPresentModes', ctypes.POINTER(ctypes.c_int)),
    ]

descriptor = {
    'extends': {
        'VkSwapchainCreateInfoKHR',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_SWAPCHAIN_PRESENT_MODES_CREATE_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'presentModeCount': {'python_name': ['present', 'mode', 'count']},
        'pPresentModes': {'python_name': ['p', 'present', 'modes'], 'len': [['presentModeCount']], 'type': 'VkPresentModeKHR'},
    }
}
