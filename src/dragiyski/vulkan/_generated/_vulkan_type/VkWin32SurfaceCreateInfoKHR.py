import ctypes

class VkWin32SurfaceCreateInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('hinstance', ctypes.c_void_p),
        ('hwnd', ctypes.c_void_p),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkCreateWin32SurfaceKHR',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'hinstance': 'hinstance',
        'hwnd': 'hwnd',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_win32_surface',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkWin32SurfaceCreateFlagsKHR',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_WIN32_SURFACE_CREATE_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_WIN32_SURFACE_CREATE_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkWin32SurfaceCreateInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'hinstance': ctypes.c_void_p,
    'hwnd': ctypes.c_void_p,
}
