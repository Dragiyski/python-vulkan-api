import ctypes

class VkImportMemoryWin32HandleInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('handleType', ctypes.c_uint32),
        ('handle', ctypes.c_void_p),
    ]

    _init_ = []
    _extends_ = {
        'VkMemoryAllocateInfo',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'handleType': 'handle_type',
        'handle': 'handle',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_external_memory_win32',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'handleType': 'VkExternalMemoryHandleTypeFlagsNV',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_IMPORT_MEMORY_WIN32_HANDLE_INFO_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMPORT_MEMORY_WIN32_HANDLE_INFO_NV
        for function in self._init_:
            function(self, *args, **kwargs)

VkImportMemoryWin32HandleInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'handleType': ctypes.c_uint32,
    'handle': ctypes.c_void_p,
}
