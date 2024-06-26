import ctypes

class VkSubresourceLayout2KHR(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkImageCompressionPropertiesEXT',
        'VkSubresourceHostMemcpySizeEXT',
    }
    _includes_ = {
        'VkSubresourceLayout',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = {
        'vkGetDeviceImageSubresourceLayoutKHR',
        'vkGetImageSubresourceLayout2KHR',
    }
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'subresourceLayout': 'subresource_layout',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_maintenance5',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_SUBRESOURCE_LAYOUT_2_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_SUBRESOURCE_LAYOUT_2_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkSubresourceLayout import VkSubresourceLayout

VkSubresourceLayout2KHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('subresourceLayout', VkSubresourceLayout),
]

VkSubresourceLayout2KHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'subresourceLayout': VkSubresourceLayout,
}
