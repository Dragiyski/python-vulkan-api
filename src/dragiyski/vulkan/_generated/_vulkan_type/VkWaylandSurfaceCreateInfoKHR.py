import ctypes

class VkWaylandSurfaceCreateInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('display', ctypes.c_void_p),
        ('surface', ctypes.c_void_p),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkCreateWaylandSurfaceKHR',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'display': 'display',
        'surface': 'surface',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_wayland_surface',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkWaylandSurfaceCreateFlagsKHR',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_WAYLAND_SURFACE_CREATE_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_WAYLAND_SURFACE_CREATE_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkWaylandSurfaceCreateInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'display': ctypes.c_void_p,
    'surface': ctypes.c_void_p,
}
