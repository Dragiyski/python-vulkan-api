import ctypes

class VkSwapchainPresentScalingCreateInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('scalingBehavior', ctypes.c_uint32),
        ('presentGravityX', ctypes.c_uint32),
        ('presentGravityY', ctypes.c_uint32),
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
        'scalingBehavior': 'scaling_behavior',
        'presentGravityX': 'present_gravity_x',
        'presentGravityY': 'present_gravity_y',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_swapchain_maintenance1',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'scalingBehavior': 'VkPresentScalingFlagsEXT',
        'presentGravityX': 'VkPresentGravityFlagsEXT',
        'presentGravityY': 'VkPresentGravityFlagsEXT',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_SWAPCHAIN_PRESENT_SCALING_CREATE_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_SWAPCHAIN_PRESENT_SCALING_CREATE_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkSwapchainPresentScalingCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'scalingBehavior': ctypes.c_uint32,
    'presentGravityX': ctypes.c_uint32,
    'presentGravityY': ctypes.c_uint32,
}
