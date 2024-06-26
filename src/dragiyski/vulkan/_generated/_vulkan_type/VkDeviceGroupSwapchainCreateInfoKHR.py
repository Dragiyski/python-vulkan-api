import ctypes

class VkDeviceGroupSwapchainCreateInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('modes', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkSwapchainCreateInfoKHR',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'modes': 'modes',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_device_group',
        'VK_KHR_swapchain',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'modes': 'VkDeviceGroupPresentModeFlagsKHR',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_DEVICE_GROUP_SWAPCHAIN_CREATE_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_GROUP_SWAPCHAIN_CREATE_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkDeviceGroupSwapchainCreateInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'modes': ctypes.c_uint32,
}
