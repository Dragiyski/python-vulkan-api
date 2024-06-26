import ctypes

class VkIOSSurfaceCreateInfoMVK(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('pView', ctypes.c_void_p),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkCreateIOSSurfaceMVK',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'pView': 'view',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_MVK_ios_surface',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkIOSSurfaceCreateFlagsMVK',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_IOS_SURFACE_CREATE_INFO_MVK'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_IOS_SURFACE_CREATE_INFO_MVK
        for function in self._init_:
            function(self, *args, **kwargs)

VkIOSSurfaceCreateInfoMVK._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'pView': ctypes.c_void_p,
}
