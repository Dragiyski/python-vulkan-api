import ctypes

class VkReleaseSwapchainImagesInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('swapchain', ctypes.c_void_p),
        ('imageIndexCount', ctypes.c_uint32),
        ('pImageIndices', ctypes.POINTER(ctypes.c_uint32)),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkReleaseSwapchainImagesEXT',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'swapchain': 'swapchain',
        'imageIndexCount': 'image_index_count',
        'pImageIndices': 'image_indices',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_swapchain_maintenance1',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_RELEASE_SWAPCHAIN_IMAGES_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_RELEASE_SWAPCHAIN_IMAGES_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkReleaseSwapchainImagesInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'swapchain': ctypes.c_void_p,
    'imageIndexCount': ctypes.c_uint32,
    'pImageIndices': ctypes.POINTER(ctypes.c_uint32),
}
