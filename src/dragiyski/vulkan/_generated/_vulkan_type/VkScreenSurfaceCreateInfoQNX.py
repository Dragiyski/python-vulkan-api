import ctypes

class VkScreenSurfaceCreateInfoQNX(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('context', ctypes.c_void_p),
        ('window', ctypes.c_void_p),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkCreateScreenSurfaceQNX',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'context': 'context',
        'window': 'window',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_QNX_screen_surface',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkScreenSurfaceCreateFlagsQNX',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_SCREEN_SURFACE_CREATE_INFO_QNX'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_SCREEN_SURFACE_CREATE_INFO_QNX
        for function in self._init_:
            function(self, *args, **kwargs)

VkScreenSurfaceCreateInfoQNX._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'context': ctypes.c_void_p,
    'window': ctypes.c_void_p,
}
