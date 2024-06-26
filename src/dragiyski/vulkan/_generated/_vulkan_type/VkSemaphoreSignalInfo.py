import ctypes

class VkSemaphoreSignalInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('semaphore', ctypes.c_void_p),
        ('value', ctypes.c_uint64),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkSignalSemaphore',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'semaphore': 'semaphore',
        'value': 'value',
    }
    _vk_versions_ = {
        (1, 2),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_SEMAPHORE_SIGNAL_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_SEMAPHORE_SIGNAL_INFO
        for function in self._init_:
            function(self, *args, **kwargs)

VkSemaphoreSignalInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'semaphore': ctypes.c_void_p,
    'value': ctypes.c_uint64,
}
