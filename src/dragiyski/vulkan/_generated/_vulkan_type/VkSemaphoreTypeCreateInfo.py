import ctypes

class VkSemaphoreTypeCreateInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('semaphoreType', ctypes.c_int),
        ('initialValue', ctypes.c_uint64),
    ]

    _init_ = []
    _extends_ = {
        'VkPhysicalDeviceExternalSemaphoreInfo',
        'VkSemaphoreCreateInfo',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'semaphoreType': 'semaphore_type',
        'initialValue': 'initial_value',
    }
    _vk_versions_ = {
        (1, 2),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'semaphoreType': 'VkSemaphoreType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_SEMAPHORE_TYPE_CREATE_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_SEMAPHORE_TYPE_CREATE_INFO
        for function in self._init_:
            function(self, *args, **kwargs)

VkSemaphoreTypeCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'semaphoreType': ctypes.c_int,
    'initialValue': ctypes.c_uint64,
}
