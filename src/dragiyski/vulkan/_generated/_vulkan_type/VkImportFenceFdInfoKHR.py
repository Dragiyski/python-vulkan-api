import ctypes

class VkImportFenceFdInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('fence', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('handleType', ctypes.c_uint32),
        ('fd', ctypes.c_int),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkImportFenceFdKHR',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'fence': 'fence',
        'flags': 'flags',
        'handleType': 'handle_type',
        'fd': 'fd',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_external_fence_fd',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkFenceImportFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_IMPORT_FENCE_FD_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMPORT_FENCE_FD_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkImportFenceFdInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'fence': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'handleType': ctypes.c_uint32,
    'fd': ctypes.c_int,
}
