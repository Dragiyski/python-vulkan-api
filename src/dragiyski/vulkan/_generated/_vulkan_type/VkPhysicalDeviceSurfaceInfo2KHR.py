import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('surface', ctypes.c_void_p),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkSurfaceFullScreenExclusiveInfoEXT',
        'VkSurfaceFullScreenExclusiveWin32InfoEXT',
        'VkSurfacePresentModeEXT',
    },
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkGetDeviceGroupSurfacePresentModes2EXT',
        'vkGetPhysicalDeviceSurfaceCapabilities2KHR',
        'vkGetPhysicalDeviceSurfaceFormats2KHR',
        'vkGetPhysicalDeviceSurfacePresentModes2EXT',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SURFACE_INFO_2_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'surface': {'python_name': ['surface']},
    }
}
