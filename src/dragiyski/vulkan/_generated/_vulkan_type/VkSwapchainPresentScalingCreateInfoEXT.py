import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('scalingBehavior', ctypes.c_uint32),
        ('presentGravityX', ctypes.c_uint32),
        ('presentGravityY', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_SWAPCHAIN_PRESENT_SCALING_CREATE_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'scalingBehavior': {'python_name': ['scaling', 'behavior'], 'type': 'VkPresentScalingFlagsEXT'},
        'presentGravityX': {'python_name': ['present', 'gravity', 'x'], 'type': 'VkPresentGravityFlagsEXT'},
        'presentGravityY': {'python_name': ['present', 'gravity', 'y'], 'type': 'VkPresentGravityFlagsEXT'},
    }
}
