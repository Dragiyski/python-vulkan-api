import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('fullScreenExclusive', ctypes.c_int),
    ]

descriptor = {
    'extends': {
        'VkPhysicalDeviceSurfaceInfo2KHR',
        'VkSwapchainCreateInfoKHR',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_SURFACE_FULL_SCREEN_EXCLUSIVE_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'fullScreenExclusive': {'python_name': ['full', 'screen', 'exclusive'], 'type': 'VkFullScreenExclusiveEXT'},
    }
}
