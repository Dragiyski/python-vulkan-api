import ctypes

class VkXlibSurfaceCreateInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('dpy', ctypes.c_void_p),
        ('window', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkCreateXlibSurfaceKHR',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'dpy': 'dpy',
        'window': 'window',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_xlib_surface',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkXlibSurfaceCreateFlagsKHR',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_XLIB_SURFACE_CREATE_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_XLIB_SURFACE_CREATE_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkXlibSurfaceCreateInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'dpy': ctypes.c_void_p,
    'window': ctypes.c_uint32,
}
