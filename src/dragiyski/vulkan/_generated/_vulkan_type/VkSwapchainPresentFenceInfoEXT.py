import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('swapchainCount', ctypes.c_uint32),
        ('pFences', ctypes.POINTER(ctypes.c_void_p)),
    ]

descriptor = {
    'extends': {
        'VkPresentInfoKHR',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_SWAPCHAIN_PRESENT_FENCE_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'swapchainCount': {'python_name': ['swapchain', 'count']},
        'pFences': {'python_name': ['p', 'fences'], 'len': [['swapchainCount']]},
    }
}
