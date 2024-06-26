import ctypes

class VkAcquireNextImageInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('swapchain', ctypes.c_void_p),
        ('timeout', ctypes.c_uint64),
        ('semaphore', ctypes.c_void_p),
        ('fence', ctypes.c_void_p),
        ('deviceMask', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkAcquireNextImage2KHR',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'swapchain': 'swapchain',
        'timeout': 'timeout',
        'semaphore': 'semaphore',
        'fence': 'fence',
        'deviceMask': 'device_mask',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_device_group',
        'VK_KHR_swapchain',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_ACQUIRE_NEXT_IMAGE_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_ACQUIRE_NEXT_IMAGE_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkAcquireNextImageInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'swapchain': ctypes.c_void_p,
    'timeout': ctypes.c_uint64,
    'semaphore': ctypes.c_void_p,
    'fence': ctypes.c_void_p,
    'deviceMask': ctypes.c_uint32,
}
