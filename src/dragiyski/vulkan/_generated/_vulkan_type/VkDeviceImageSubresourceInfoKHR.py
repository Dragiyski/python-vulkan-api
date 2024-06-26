import ctypes

class VkDeviceImageSubresourceInfoKHR(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkImageCreateInfo',
        'VkImageSubresource2KHR',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkGetDeviceImageSubresourceLayoutKHR',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'pCreateInfo': 'create_info',
        'pSubresource': 'subresource',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_maintenance5',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_DEVICE_IMAGE_SUBRESOURCE_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_IMAGE_SUBRESOURCE_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkImageCreateInfo import VkImageCreateInfo
from .VkImageSubresource2KHR import VkImageSubresource2KHR

VkDeviceImageSubresourceInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pCreateInfo', ctypes.POINTER(VkImageCreateInfo)),
    ('pSubresource', ctypes.POINTER(VkImageSubresource2KHR)),
]

VkDeviceImageSubresourceInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pCreateInfo': ctypes.POINTER(VkImageCreateInfo),
    'pSubresource': ctypes.POINTER(VkImageSubresource2KHR),
}
