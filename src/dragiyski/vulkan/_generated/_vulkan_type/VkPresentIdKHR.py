import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('swapchainCount', ctypes.c_uint32),
        ('pPresentIds', ctypes.POINTER(ctypes.c_uint64)),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PRESENT_ID_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'swapchainCount': {'python_name': ['swapchain', 'count']},
        'pPresentIds': {'python_name': ['p', 'present', 'ids'], 'len': [['swapchainCount']]},
    }
}
