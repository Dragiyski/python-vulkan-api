import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent2D import CType as VkExtent2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('surface', ctypes.c_void_p),
    ('minImageCount', ctypes.c_uint32),
    ('imageFormat', ctypes.c_int),
    ('imageColorSpace', ctypes.c_int),
    ('imageExtent', VkExtent2D),
    ('imageArrayLayers', ctypes.c_uint32),
    ('imageUsage', ctypes.c_uint32),
    ('imageSharingMode', ctypes.c_int),
    ('queueFamilyIndexCount', ctypes.c_uint32),
    ('pQueueFamilyIndices', ctypes.POINTER(ctypes.c_uint32)),
    ('preTransform', ctypes.c_uint32),
    ('compositeAlpha', ctypes.c_uint32),
    ('presentMode', ctypes.c_int),
    ('clipped', ctypes.c_uint32),
    ('oldSwapchain', ctypes.c_void_p),
]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkDeviceGroupSwapchainCreateInfoKHR',
        'VkImageCompressionControlEXT',
        'VkImageFormatListCreateInfo',
        'VkSurfaceFullScreenExclusiveInfoEXT',
        'VkSurfaceFullScreenExclusiveWin32InfoEXT',
        'VkSwapchainCounterCreateInfoEXT',
        'VkSwapchainDisplayNativeHdrCreateInfoAMD',
        'VkSwapchainLatencyCreateInfoNV',
        'VkSwapchainPresentBarrierCreateInfoNV',
        'VkSwapchainPresentModesCreateInfoEXT',
        'VkSwapchainPresentScalingCreateInfoEXT',
    },
    'includes': {
        'VkExtent2D',
    },
    'included_in': set(),
    'input_of': {
        'vkCreateSharedSwapchainsKHR',
        'vkCreateSwapchainKHR',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_SWAPCHAIN_CREATE_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkSwapchainCreateFlagsKHR'},
        'surface': {'python_name': ['surface']},
        'minImageCount': {'python_name': ['min', 'image', 'count']},
        'imageFormat': {'python_name': ['image', 'format'], 'type': 'VkFormat'},
        'imageColorSpace': {'python_name': ['image', 'color', 'space'], 'type': 'VkColorSpaceKHR'},
        'imageExtent': {'python_name': ['image', 'extent'], 'type': 'VkExtent2D'},
        'imageArrayLayers': {'python_name': ['image', 'array', 'layers']},
        'imageUsage': {'python_name': ['image', 'usage'], 'type': 'VkImageUsageFlags'},
        'imageSharingMode': {'python_name': ['image', 'sharing', 'mode'], 'type': 'VkSharingMode'},
        'queueFamilyIndexCount': {'python_name': ['queue', 'family', 'index', 'count']},
        'pQueueFamilyIndices': {'python_name': ['p', 'queue', 'family', 'indices'], 'len': [['queueFamilyIndexCount']]},
        'preTransform': {'python_name': ['pre', 'transform'], 'type': 'VkSurfaceTransformFlagBitsKHR'},
        'compositeAlpha': {'python_name': ['composite', 'alpha'], 'type': 'VkCompositeAlphaFlagBitsKHR'},
        'presentMode': {'python_name': ['present', 'mode'], 'type': 'VkPresentModeKHR'},
        'clipped': {'python_name': ['clipped']},
        'oldSwapchain': {'python_name': ['old', 'swapchain']},
    }
}
