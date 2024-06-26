import ctypes

class VkImportSemaphoreWin32HandleInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('semaphore', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('handleType', ctypes.c_uint32),
        ('handle', ctypes.c_void_p),
        ('name', ctypes.c_wchar_p),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkImportSemaphoreWin32HandleKHR',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'semaphore': 'semaphore',
        'flags': 'flags',
        'handleType': 'handle_type',
        'handle': 'handle',
        'name': 'name',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_external_semaphore_win32',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkSemaphoreImportFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_IMPORT_SEMAPHORE_WIN32_HANDLE_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMPORT_SEMAPHORE_WIN32_HANDLE_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkImportSemaphoreWin32HandleInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'semaphore': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'handleType': ctypes.c_uint32,
    'handle': ctypes.c_void_p,
    'name': ctypes.c_wchar_p,
}
