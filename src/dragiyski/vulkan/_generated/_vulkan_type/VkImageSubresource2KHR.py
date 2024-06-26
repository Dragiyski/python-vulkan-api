import ctypes

class VkImageSubresource2KHR(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkImageSubresource',
    }
    _included_in_ = {
        'VkDeviceImageSubresourceInfoKHR',
    }
    _input_of_ = {
        'vkGetImageSubresourceLayout2KHR',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'imageSubresource': 'image_subresource',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_maintenance5',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_IMAGE_SUBRESOURCE_2_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_SUBRESOURCE_2_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkImageSubresource import VkImageSubresource

VkImageSubresource2KHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('imageSubresource', VkImageSubresource),
]

VkImageSubresource2KHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'imageSubresource': VkImageSubresource,
}
