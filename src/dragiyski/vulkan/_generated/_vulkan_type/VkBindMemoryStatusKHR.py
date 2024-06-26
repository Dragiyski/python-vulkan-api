import ctypes

class VkBindMemoryStatusKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pResult', ctypes.POINTER(ctypes.c_int)),
    ]

    _init_ = []
    _extends_ = {
        'VkBindBufferMemoryInfo',
        'VkBindImageMemoryInfo',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'pResult': 'result',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_maintenance6',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'pResult': 'VkResult',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_BIND_MEMORY_STATUS_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_BIND_MEMORY_STATUS_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkBindMemoryStatusKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pResult': ctypes.POINTER(ctypes.c_int),
}
