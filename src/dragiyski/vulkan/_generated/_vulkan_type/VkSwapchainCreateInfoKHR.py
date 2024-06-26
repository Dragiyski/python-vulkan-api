import ctypes

class VkSwapchainCreateInfoKHR(ctypes.Structure):
    _init_ = []
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
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'surface': 'surface',
        'minImageCount': 'min_image_count',
        'imageFormat': 'image_format',
        'imageColorSpace': 'image_color_space',
        'imageExtent': 'image_extent',
        'imageArrayLayers': 'image_array_layers',
        'imageUsage': 'image_usage',
        'imageSharingMode': 'image_sharing_mode',
        'queueFamilyIndexCount': 'queue_family_index_count',
        'pQueueFamilyIndices': 'queue_family_indices',
        'preTransform': 'pre_transform',
        'compositeAlpha': 'composite_alpha',
        'presentMode': 'present_mode',
        'clipped': 'clipped',
        'oldSwapchain': 'old_swapchain',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_swapchain',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkSwapchainCreateFlagsKHR',
        'imageFormat': 'VkFormat',
        'imageColorSpace': 'VkColorSpaceKHR',
        'imageUsage': 'VkImageUsageFlags',
        'imageSharingMode': 'VkSharingMode',
        'presentMode': 'VkPresentModeKHR',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_SWAPCHAIN_CREATE_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_SWAPCHAIN_CREATE_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkExtent2D import VkExtent2D

VkSwapchainCreateInfoKHR._fields_ = [
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

VkSwapchainCreateInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'surface': ctypes.c_void_p,
    'minImageCount': ctypes.c_uint32,
    'imageFormat': ctypes.c_int,
    'imageColorSpace': ctypes.c_int,
    'imageExtent': VkExtent2D,
    'imageArrayLayers': ctypes.c_uint32,
    'imageUsage': ctypes.c_uint32,
    'imageSharingMode': ctypes.c_int,
    'queueFamilyIndexCount': ctypes.c_uint32,
    'pQueueFamilyIndices': ctypes.POINTER(ctypes.c_uint32),
    'preTransform': ctypes.c_uint32,
    'compositeAlpha': ctypes.c_uint32,
    'presentMode': ctypes.c_int,
    'clipped': ctypes.c_uint32,
    'oldSwapchain': ctypes.c_void_p,
}
