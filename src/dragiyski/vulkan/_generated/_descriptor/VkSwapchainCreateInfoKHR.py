from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSwapchainCreateInfoKHR'
_member_list_ = ['sType', 'pNext', 'flags', 'surface', 'minImageCount', 'imageFormat', 'imageColorSpace', 'imageExtent', 'imageArrayLayers', 'imageUsage', 'imageSharingMode', 'queueFamilyIndexCount', 'pQueueFamilyIndices', 'preTransform', 'compositeAlpha', 'presentMode', 'clipped', 'oldSwapchain']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_SWAPCHAIN_CREATE_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkSwapchainCreateFlagsKHR',
        'enum': 'VkSwapchainCreateFlagsKHR',
        'is_string': False,
    },
    'surface': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'minImageCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'imageFormat': {
        'type': CIntType('c_int'),
        'type_name': 'VkFormat',
        'enum': 'VkFormat',
        'is_string': False,
    },
    'imageColorSpace': {
        'type': CIntType('c_int'),
        'type_name': 'VkColorSpaceKHR',
        'enum': 'VkColorSpaceKHR',
        'is_string': False,
    },
    'imageExtent': {
        'type': CComplexType('VkExtent2D'),
        'type_name': 'VkExtent2D',
        'structure': 'VkExtent2D',
        'is_string': False,
    },
    'imageArrayLayers': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'imageUsage': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkImageUsageFlags',
        'enum': 'VkImageUsageFlags',
        'is_string': False,
    },
    'imageSharingMode': {
        'type': CIntType('c_int'),
        'type_name': 'VkSharingMode',
        'enum': 'VkSharingMode',
        'is_string': False,
    },
    'queueFamilyIndexCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pQueueFamilyIndices': {
        'type': CPointerType(CIntType('c_uint32')),
        'length': [['queueFamilyIndexCount']],
        'is_string': False,
    },
    'preTransform': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkSurfaceTransformFlagBitsKHR',
        'is_string': False,
    },
    'compositeAlpha': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkCompositeAlphaFlagBitsKHR',
        'is_string': False,
    },
    'presentMode': {
        'type': CIntType('c_int'),
        'type_name': 'VkPresentModeKHR',
        'enum': 'VkPresentModeKHR',
        'is_string': False,
    },
    'clipped': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'oldSwapchain': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
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
}
_includes_ = {
    'VkExtent2D',
}
_included_in_ = set()
_input_of_ = {
    'vkCreateSharedSwapchainsKHR',
    'vkCreateSwapchainKHR',
}
_output_of_ = set()
