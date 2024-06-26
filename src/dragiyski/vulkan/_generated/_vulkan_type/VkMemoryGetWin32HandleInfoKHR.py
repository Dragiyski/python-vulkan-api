import ctypes

class VkMemoryGetWin32HandleInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('memory', ctypes.c_void_p),
        ('handleType', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkGetMemoryWin32HandleKHR',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'memory': 'memory',
        'handleType': 'handle_type',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_external_memory_win32',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_MEMORY_GET_WIN32_HANDLE_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_MEMORY_GET_WIN32_HANDLE_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkMemoryGetWin32HandleInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'memory': ctypes.c_void_p,
    'handleType': ctypes.c_uint32,
}
