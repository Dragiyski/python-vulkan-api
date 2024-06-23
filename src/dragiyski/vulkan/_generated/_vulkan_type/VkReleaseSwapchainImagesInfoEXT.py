import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('swapchain', ctypes.c_void_p),
        ('imageIndexCount', ctypes.c_uint32),
        ('pImageIndices', ctypes.POINTER(ctypes.c_uint32)),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkReleaseSwapchainImagesEXT',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_RELEASE_SWAPCHAIN_IMAGES_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'swapchain': {'python_name': ['swapchain'], 'externsync': [['true']]},
        'imageIndexCount': {'python_name': ['image', 'index', 'count']},
        'pImageIndices': {'python_name': ['p', 'image', 'indices'], 'len': [['imageIndexCount']]},
    }
}
