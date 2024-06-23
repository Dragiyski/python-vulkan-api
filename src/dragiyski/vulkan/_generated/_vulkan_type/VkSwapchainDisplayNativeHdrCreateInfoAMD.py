import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('localDimmingEnable', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_SWAPCHAIN_DISPLAY_NATIVE_HDR_CREATE_INFO_AMD', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'localDimmingEnable': {'python_name': ['local', 'dimming', 'enable']},
    }
}
